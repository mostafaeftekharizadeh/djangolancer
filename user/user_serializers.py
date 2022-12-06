import random
import datetime
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from library.serializers import ModelOwnerSerializer
from rest_framework.authtoken.models import Token
from .models import  Otp, Party, Profile, Vote


class OtpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, required=False)
    token = serializers.CharField(required=False)
    code = serializers.CharField(write_only=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Otp
        fields = ['token', 'code', 'email', 'created_at']
    def create(self, validated_data):
        if 'code' in validated_data:
            try:
                otp = Otp.objects.get(code=validated_data['code'],
                                token=validated_data['token'],
                                activated_at__isnull = True,
                                created_at__gte = datetime.datetime.now() -  datetime.timedelta(minutes=settings.OTP_EXPIRE_TIME)
                                )
                otp.activated_at = datetime.datetime.now()
                otp.save()
                user = otp.user
                user.is_active = True
                user.save()
            except Exception as e:
                raise serializers.ValidationError({"no_feild_erros": "otp/token not valid."})
            return otp
        else:
            if settings.DEBUG:
                code = 12345
            else:
                code = None
            user = User.objects.get(email=validated_data['email'])
            otp_count = Otp.objects.filter(user=user,
                                    created_at__gte = datetime.datetime.now() -  datetime.timedelta(minutes=settings.OTP_EXPIRE_TIME)).count()
            if otp_count > 0:
                raise serializers.ValidationError({"no_feild_erros": "otp rate limit reached."})
            otp = Otp.objects.create(user=user, code=code)
        return otp

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=False)
    token = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'token')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        instance = getattr(self, 'instance', None)
        if instance == None:
            if "password" not in attrs or "password2" not in attrs:
                raise serializers.ValidationError({"password": "password/password2 requited."})
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        party = Party.objects.create(user = user)
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        return user

    def update(self, instance, validated_data):
        instance.email=validated_data['email']
        instance.first_name=validated_data['first_name']
        instance.last_name=validated_data['last_name']
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

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
            print(profile.city)
        if validated_data.get("gender"):
            profile.gender = validated_data.get("gender")
        if validated_data.get("age"):
            profile.age = validated_data.get("age")
        profile.save()

        return instance

class VoteSerializer(ModelOwnerSerializer):
    class Meta:
        model = Vote
        fields = ['user','voter','vote']
