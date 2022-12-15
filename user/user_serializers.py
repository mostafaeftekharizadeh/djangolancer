import random
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import get_current_timezone
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from library.serializers import ModelOwnerSerializer
from rest_framework.authtoken.models import Token
from .user_models import   Party, Otp
from .profile_models import  Profile, Vote

User = get_user_model()


def mobile_check(value):
    if not value.startswith("98"):
        if value.startswith("0"):
            value = value[1:]
        value = "98{}".format(value)
    return value
class OtpSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(write_only=True, required=False)
    token = serializers.CharField(required=False)
    code = serializers.CharField(write_only=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Otp
        fields = ['mobile', 'token', 'code', 'created_at']
    def create(self, validated_data):
        if 'code' in validated_data:
            #try:
            if 1==1:
                otp = Otp.objects.get(code=validated_data['code'],
                                token=validated_data['token'],
                                activated_at__isnull = True,
                                created_at__gte = datetime.datetime.now(tz=get_current_timezone()) -  datetime.timedelta(minutes=settings.OTP_EXPIRE_TIME)
                                )
                otp.activated_at = datetime.datetime.now(tz=get_current_timezone())
                otp.save()
            #except Exception as e:
            #    raise serializers.ValidationError({"no_feild_erros": "otp/token not valid."})
            return otp
        else:
            if settings.DEBUG:
                code = 12345
            else:
                code = None
            otp = Otp.objects.create(mobile=validated_data['mobile'], code=code)
            return otp

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(required=True,
                                    validators=[]
                                    )
    username = serializers.CharField(required=True,
                                    validators=[UniqueValidator(queryset=User.objects.all())]
                                    )
    email = serializers.EmailField(
            required=False,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=False)
    token = serializers.CharField(read_only=True, required=False)
    otp_token = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('mobile', 'username', 'password', 'password2', 'email', 'first_name', 'last_name', 'token', 'otp_token')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def validate_mobile(self, value):
        value = mobile_check(value)
        if User.objects.filter(mobile=value).count() > 0:
            raise serializers.ValidationError(_('This field must be unique.'))
        return value

    def validate(self, attrs):
        instance = getattr(self, 'instance', None)
        if instance == None:
            if "password" not in attrs or "password2" not in attrs:
                raise serializers.ValidationError({"password": "password/password2 required."})
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User(
            mobile=validated_data['mobile'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        if 'otp_token' in validated_data:
            try:
                # check if otp token is valid, then expire otp_token
                otp = Otp.objects.get(mobile=validated_data['mobile'],
                                      token=validated_data['otp_token'],
                                      activated_at__isnull=False)
                otp.save()
            except:
                raise serializers.ValidationError({"otp_token": "invalid"})
            user.set_password(validated_data['password'])
            user.is_active = True
            user.save()

            party = Party.objects.create(user = user)
            token, created = Token.objects.get_or_create(user=user)
            user.token = token.key
        else:
            otp_serializer = OtpSerializer(data={'mobile' : validated_data['mobile']})
            if otp_serializer.is_valid():
                otp_serializer.save()
            user.otp_token = otp_serializer.data['token']
        return user


    def update(self, instance, validated_data):
        instance.mobile=validated_data['mobile']
        instance.first_name=validated_data['first_name']
        instance.last_name=validated_data['last_name']
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):

    username = serializers.CharField(read_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'old_password', 'password', 'password2')

    def validate(self, attrs):
        if self.context['request'].user.check_password(attrs['old_password']) == False:
            raise serializers.ValidationError({"old_password": "Old Password is incorrect."})

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password"))
        instance.save()

        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    '''
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
            '''

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')#, 'city', 'gender', 'age')
        '''
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
        '''

    def validate(self, attrs):
        _user = self.context['request'].user
        if ('email' in attrs and
            _user.email != attrs['email'] and
            len(User.objects.filter(email=attrs['email'])) > 1):
            raise serializers.ValidationError({"email": "This field must be unique."})

        return attrs

    def update(self, instance, validated_data):
        if validated_data.get('first_name'):
            instance.first_name = validated_data.get("first_name")
        if validated_data.get('last_name'):
            instance.last_name = validated_data.get("last_name")
        if validated_data.get('email'):
            instance.email = validated_data.get("email")
        instance.save()

        profile = Profile.objects.get(user=instance)
        if validated_data.get("city"):
            profile.city = validated_data.get("city")
        if validated_data.get("gender"):
            profile.gender = validated_data.get("gender")
        if validated_data.get("age"):
            profile.age = validated_data.get("age")
        profile.save()

        return instance

class AuthTokenSerializer(serializers.Serializer):
    mobile = serializers.CharField(label=_("Mobile"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def validate(self, attrs):
        mobile = mobile_check(attrs.get('mobile'))
        password = attrs.get('password')

        if mobile and password:
            user = authenticate(mobile=mobile, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "mobile" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs

class VoteSerializer(ModelOwnerSerializer):
    class Meta:
        model = Vote
        fields = ['user','voter','vote']
