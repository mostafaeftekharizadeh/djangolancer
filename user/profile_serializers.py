from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from .user_serializers import UserSerializer, PartySerializer
from .profile_models import  (Profile,
                      Contact,
                      Skill,
                      Job,
                      Education,
                      Certificate,
                      Specialty,
                      Achievement,
                      Language,
                      WorkSample,
                      Experience,
                      SocialMedia)


class ContactSerializer(ModelOwnerSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'contact_type', 'party', 'contact']

class SkillSerializer(ModelOwnerSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill', 'party', 'level']

class JobSerializer(ModelOwnerSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title','company','description','date_start','date_end']

class EducationSerializer(ModelOwnerSerializer):
    class Meta:
        model = Education
        fields = ['id', 'party', 'degree','uni_name','major','date_start','date_end']

class CertificateSerializer(ModelOwnerSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'party', 'name','description','Institution_name','date_start','date_end']
class SpecialtySerializer(ModelOwnerSerializer):
    class Meta:
        model = Specialty
        fields = ['id', 'party', 'level','description','Institution_name','date_start','date_end']
class AchievementSerializer(ModelOwnerSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'party', 'title','event','description','date_start','date_end']

class LanguageSerializer(ModelOwnerSerializer):
    class Meta:
        model = Language
        fields = ['id', 'party', 'language','talking','writing','comprehension']

class WorkSampleSerializer(ModelOwnerSerializer):
    class Meta:
        model = WorkSample
        fields = ['id', 'party', 'title','skill','description']

class ExperienceSerializer(ModelOwnerSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'party',"work_place", 'title','skill','description',"date_start", "date_end"]

class SocialMediaSerializer(ModelOwnerSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'party', 'name','userid','phone','link','date_start','date_end']

class AvatarSerializer(ModelOwnerSerializer):
    avatar = serializers.ImageField(write_only=True, required=True)
    class Meta:
        model = Profile
        fields = ['party', 'avatar']
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class ProfileSerializer(ModelOwnerSerializer):
    contacts = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    jobs = serializers.SerializerMethodField()
    educations = serializers.SerializerMethodField()
    certificates = serializers.SerializerMethodField()
    specialties = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    work_samples = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = "__all__"
    def get_contacts(self, obj):
        qs = obj.party.party_contact.all()
        return ContactSerializer(qs, context=self.context, many=True).data
    def get_skills(self, obj):
        qs = obj.party.party_skill.all()
        return SkillSerializer(qs, context=self.context, many=True).data
    def get_jobs(self, obj):
        qs = obj.party.party_job.all()
        return JobSerializer(qs, context=self.context, many=True).data
    def get_educations(self, obj):
        qs = obj.party.party_education.all()
        return EducationSerializer(qs, context=self.context, many=True).data
    def get_certificates(self, obj):
        qs = obj.party.party_certificate.all()
        return CertificateSerializer(qs, context=self.context, many=True).data
    def get_specialties(self, obj):
        qs = obj.party.party_speciality.all()
        return SpecialtySerializer(qs, context=self.context, many=True).data
    def get_achievements(self, obj):
        qs = obj.party.party_achievement.all()
        return AchievementSerializer(qs, context=self.context, many=True).data
    def get_languages(self, obj):
        qs = obj.party.party_language.all()
        return LanguageSerializer(qs, context=self.context, many=True).data
    def get_work_samples(self, obj):
        qs = obj.party.party_worksample.all()
        return WorkSampleSerializer(qs, context=self.context, many=True).data
    def get_experience(self, obj):
        qs = obj.party.party_experience.all()
        return ExperienceSerializer(qs, context=self.context, many=True).data
    def get_social_medias(self, obj):
        qs = obj.party.party_socialmedia.all()
        return SocialMediaSerializer(qs, context=self.context, many=True).data
    def get_user(self, obj):
        return UserSerializer(obj.party.user, context=self.context, many=False).data
