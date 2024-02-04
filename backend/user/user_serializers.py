"""
User serializer module
"""
import datetime
import re
import logging
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import get_current_timezone
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db.models import Avg, Window
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from library.serializers import ModelSerializer, ModelOwnerSerializer
from money.models import Wallet
from .user_models import Party, Otp
from .profile_models import Profile, Vote

User = get_user_model()

_logger = logging.getLogger("midlancer.api.user.user")


def format_mobile_number(value):
    """
    format mobile number to 98XXXXXXXX
    """
    return re.sub(r"^([0\+]+(98)?)|^98|^0?", "98", value)


class OtpSerializer(serializers.ModelSerializer):
    """
    Otp model serializer
    """

    mobile = serializers.CharField(write_only=True, required=False)
    token = serializers.CharField(required=False)
    code = serializers.CharField(write_only=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        """
        Meta Class
        """

        model = Otp
        fields = ["mobile", "token", "code", "created_at"]

    def create(self, validated_data):
        """
        override post to otp endpoint
        if code is sent check if token is exists then expire it and return new token
        """
        mobile = format_mobile_number(validated_data["mobile"])
        if "code" in validated_data:
            try:
                otp = Otp.objects.get(
                    mobile=mobile,
                    code=validated_data["code"],
                    token=validated_data["token"],
                    activated_at__isnull=True,
                    created_at__gte=datetime.datetime.now(tz=get_current_timezone())
                    - datetime.timedelta(minutes=settings.OTP_EXPIRE_TIME),
                )
                otp.activated_at = datetime.datetime.now(tz=get_current_timezone())
                otp.save()
            except Exception as exc:
                _logger.error(exc)
                raise serializers.ValidationError(
                    {"no_feild_erros": "otp/token not valid."}
                )
            return otp
        if settings.DEBUG or mobile.startswith("988"):
            code = 12345
        else:
            code = None
        otp = Otp.objects.create(mobile=mobile, code=code)

        if not settings.DEBUG:
            otp.send_sms()
        return otp


class PartySerializer(serializers.ModelSerializer):
    """
    Party model serializer
    """

    class Meta:
        """
        Meta Class
        """

        model = Party
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """
    User model serializer
    """

    mobile = serializers.CharField(write_only=True, required=True, validators=[])
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        trim_whitespace=False,
        write_only=True,
        required=False,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=False)
    token = serializers.CharField(read_only=True, required=False)
    otp_token = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False, default="")
    last_name = serializers.CharField(required=False, default="")

    class Meta:
        """
        Meta Class
        """

        model = User
        fields = (
            "id",
            "mobile",
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
            "token",
            "otp_token",
        )

    def validate_mobile(self, value):
        """
        check if mobile number not exists
        """
        value = format_mobile_number(value)
        if User.objects.filter(mobile=value).count() > 0:
            raise serializers.ValidationError(_("This field must be unique."))
        return value

    def validate(self, attrs):
        """
        serializer global validation
        """
        instance = getattr(self, "instance", None)
        if instance is None:
            if "password" not in attrs or "password2" not in attrs:
                raise serializers.ValidationError(
                    {"password": "password/password2 required."}
                )
            if attrs["password"] != attrs["password2"]:
                raise serializers.ValidationError(
                    {"password": "Password fields didn't match."}
                )
        return attrs

    def create(self, validated_data):
        """
        override post endpoint
        check if otp_token is not provided , so first we need to send
        otp_token to user mobile to verify user mobile
        create Party, Profile, Wallet(maybe its better to create them
        with signal on User creation)
        """
        user = User(
            mobile=format_mobile_number(validated_data["mobile"]),
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        if "otp_token" in validated_data:
            try:
                # check if otp token is valid, then expire otp_token
                otp = Otp.objects.get(
                    mobile=format_mobile_number(validated_data["mobile"]),
                    token=validated_data["otp_token"],
                    activated_at__isnull=False,
                )
                otp.save()
            except Exception as exc:
                _logger.error(exc)
                raise serializers.ValidationError({"otp_token": "invalid"})
            user.set_password(validated_data["password"])
            user.is_active = True
            user.save()

            party = Party.objects.create(user=user)
            Profile.objects.create(party=party)
            Wallet.objects.create(party=party)
            token, created = Token.objects.get_or_create(user=user)
            user.token = token.key
        else:
            otp_serializer = OtpSerializer(
                data={"mobile": format_mobile_number(validated_data["mobile"])}
            )
            if otp_serializer.is_valid():
                otp_serializer.save()
            user.otp_token = otp_serializer.data["token"]
        return user


class ForgetPasswordSerializer(serializers.ModelSerializer):
    """
    change password serializer
    """

    mobile = serializers.CharField(required=True)
    otp_token = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        trim_whitespace=False,
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        """
        Meta Class
        """

        model = User
        fields = ("mobile", "otp_token", "password", "password2")

    def validate(self, attrs):
        """
        global validation
        """
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def update(self, instance, validated_data):
        """
        override Update endpoint
        we need to check if the user has access to change password
        with OTP validation
        """
        try:
            # check if otp token is valid, then expire otp_token
            otp = Otp.objects.get(
                mobile=format_mobile_number(validated_data["mobile"]),
                token=validated_data["otp_token"],
                activated_at__isnull=False,
            )
            otp.save()
        except Exception as exc:
            _logger.error(exc)
            raise serializers.ValidationError({"otp_token": "invalid"})
        user = User.objects.get(mobile=otp.mobile)
        user.set_password(validated_data.get("password"))
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    change password serializer
    """

    username = serializers.CharField(required=True)
    old_password = serializers.CharField(trim_whitespace=False, write_only=True)
    password = serializers.CharField(
        trim_whitespace=False,
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        """
        Meta Class
        """

        model = User
        fields = (
            "username",
            "old_password",
            "password",
            "password2",
        )

    def validate(self, attrs):
        """
        global validation
        """
        user = User.objects.get(username=attrs.get("username"))
        if not user:
            raise serializers.ValidationError({"user": "user not found."})
        print(user.check_password(attrs.get("old_password")))
        if user.check_password(attrs.get("old_password")) == False:
            raise serializers.ValidationError({"password": "Old password incorrect."})
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def update(self, instance, validated_data):
        """
        override Update endpoint
        we need to check if the user has access to change password
        with OTP validation
        """
        user = User.objects.get(username=validated_data["username"])
        user.set_password(validated_data.get("password"))
        user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """
    AuthTokenSerializer to get authorization goken
    """

    mobile = serializers.CharField(label=_("Mobile"))
    password = serializers.CharField(
        trim_whitespace=False, label=_("Password"), style={"input_type": "password"}
    )

    def validate(self, attrs):
        """
        global validation
        check if username/password is valid and user is active
        """
        mobile = format_mobile_number(attrs.get("mobile"))
        password = attrs.get("password")
        print(attrs)
        print("/", password, "/")

        if mobile and password:
            user = authenticate(mobile=mobile, password=password)

            if user:
                if not user.is_active:
                    msg = _("User account is disabled.")
                    raise serializers.ValidationError(msg)
            else:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "mobile" and "password".')
            raise serializers.ValidationError(msg)

        attrs["user"] = user
        return attrs


class VoteSerializer(ModelOwnerSerializer):
    """
    Vote serializer
    """

    class Meta:
        """
        Meta Class
        """

        model = Vote
        fields = ["party", "owner", "vote", "opinion"]


class VoteSummerySerializer(ModelOwnerSerializer):
    """
    summeryze Vote serializer
    """

    user_vote = serializers.SerializerMethodField()

    def get_user_vote(self, obj):
        return Vote.objects.filter(
            owner=self.context.get("view").kwargs.get("uid")
        ).aggregate(avg_vote=Avg("vote"))["avg_vote"]

    class Meta:
        """
        Meta Class
        """

        model = Vote
        fields = ["user_vote"]
