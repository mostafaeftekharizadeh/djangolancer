from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from library.serializers import ModelOwnerSerializer
from .models import  (Party,
                      Profile,
                      Skill,
                      Job,
                      Education,
                      Certificate,
                      Specialty,
                      Achievement,
                      Language,
                      WorkSample,
                      SocialMedia,
                      Vote)


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

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
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
        user.save()
        party = Party.objects.create(user = user)
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


class SkillSerializer(ModelOwnerSerializer):
    skill_name = serializers.CharField(read_only=True, source='skill.name')
    level_name = serializers.CharField(read_only=True, source='level.name')
    class Meta:
        model = Skill
        fields = ['id', 'skill','level', 'skill_name', 'level_name']

class JobSerializer(ModelOwnerSerializer):
    class Meta:
        model = Job
        fields = ['title','company','description','date_start','date_end']

class EducationSerializer(ModelOwnerSerializer):
    class Meta:
        model = Education
        fields = ['degree','uni_name','description','date_start','date_end']

class CertificateSerializer(ModelOwnerSerializer):
    class Meta:
        model = Certificate
        fields = ['name','description','Institution_name','date_start','date_end']
class SpecialtySerializer(ModelOwnerSerializer):
    class Meta:
        model = Specialty
        fields = ['level','description','Institution_name','date_start','date_end']
class AchievementSerializer(ModelOwnerSerializer):
    class Meta:
        model = Achievement
        fields = ['title','event','description','date_start','date_end']

class LanguageSerializer(ModelOwnerSerializer):
    class Meta:
        model = Language
        fields = ['language','talking','writing','comprehension']

class WorkSampleSerializer(ModelOwnerSerializer):
    class Meta:
        model = WorkSample
        fields = ['title','skill','description']

class SocialMediaSerializer(ModelOwnerSerializer):
    class Meta:
        model = SocialMedia
        fields = ['name','userid','phone','link','date_start','date_end']

class VoteSerializer(ModelOwnerSerializer):
    class Meta:
        model = Vote
        fields = ['user','voter','vote']

class ProfileSerializer(ModelOwnerSerializer):
    skills = serializers.SerializerMethodField()
    jobs = serializers.SerializerMethodField()
    educations = serializers.SerializerMethodField()
    certificates = serializers.SerializerMethodField()
    specialties = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    work_samples = serializers.SerializerMethodField()
    social_medias = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = "__all__"
    def get_skills(self, obj):
        qs = Skill.objects.filter(party=obj.party)
        return SkillSerializer(qs, context=self.context, many=True).data
    def get_jobs(self, obj):
        qs = Job.objects.filter(party=obj.party)
        return JobSerializer(qs, context=self.context, many=True).data
    def get_educations(self, obj):
        qs = Education.objects.filter(party=obj.party)
        return EducationSerializer(qs, context=self.context, many=True).data
    def get_certificates(self, obj):
        qs = Certificate.objects.filter(party=obj.party)
        return CertificateSerializer(qs, context=self.context, many=True).data
    def get_specialties(self, obj):
        qs = Specialty.objects.filter(party=obj.party)
        return SpecialtySerializer(qs, context=self.context, many=True).data
    def get_achievements(self, obj):
        qs = Achievement.objects.filter(party=obj.party)
        return AchievementSerializer(qs, context=self.context, many=True).data
    def get_languages(self, obj):
        qs = Language.objects.filter(party=obj.party)
        return LanguageSerializer(qs, context=self.context, many=True).data
    def get_work_samples(self, obj):
        qs = WorkSample.objects.filter(party=obj.party)
        return WorkSampleSerializer(qs, context=self.context, many=True).data
    def get_social_medias(self, obj):
        qs = SocialMedia.objects.filter(party=obj.party)
        return SocialMediaSerializer(qs, context=self.context, many=True).data
    def get_user(self, obj):
        return UserSerializer(obj.party.user, context=self.context, many=False).data
