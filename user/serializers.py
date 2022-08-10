from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Maintainer, Profile

class MaintainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maintainer
        fields = ['name']


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
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
        user.save()

        profile = Profile.objects.create(user = user)


        return user

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
        print(validated_data.get("first_name"))
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
