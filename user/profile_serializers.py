from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from user.views import UserSerializer
from .models import  (Profile,
                      Skill,
                      Job,
                      Education,
                      Certificate,
                      Specialty,
                      Achievement,
                      Language,
                      WorkSample,
                      SocialMedia)


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
