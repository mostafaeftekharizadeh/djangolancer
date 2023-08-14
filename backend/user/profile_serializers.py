"""
User Profile serializers
"""
from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from .user_serializers import UserSerializer
from .profile_models import (
    Profile,
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
    SocialMedia,
)


# pylint: disable=too-many-ancestors
class ContactSerializer(ModelOwnerSerializer):
    """
    Contatc serializers
    """

    class Meta:
        model = Contact
        fields = ["id", "contact_type", "party", "contact"]


class SkillSerializer(ModelOwnerSerializer):
    """
    Skill serializers
    """

    class Meta:
        model = Skill
        # depth= 1
        fields = ["id", "skill", "party", "level"]


class JobSerializer(ModelOwnerSerializer):
    """
    Jobs serializers
    """

    class Meta:
        model = Job
        fields = ["id", "title", "company", "description", "date_start", "date_end"]


class EducationSerializer(ModelOwnerSerializer):
    """
    Educations serializers
    """

    class Meta:
        model = Education
        fields = [
            "id",
            "party",
            "degree",
            "uni_name",
            "major",
            "date_start",
            "date_end",
        ]


class CertificateSerializer(ModelOwnerSerializer):
    """
    Certificates serializers
    """

    class Meta:
        model = Certificate
        fields = [
            "id",
            "party",
            "name",
            "description",
            "Institution_name",
            "date_start",
            "date_end",
        ]


class SpecialtySerializer(ModelOwnerSerializer):
    """
    Specialty serializers
    """

    class Meta:
        model = Specialty
        fields = [
            "id",
            "party",
            "level",
            "description",
            "Institution_name",
            "date_start",
            "date_end",
        ]


class AchievementSerializer(ModelOwnerSerializer):
    """
    Achivments serializers
    """

    class Meta:
        model = Achievement
        fields = [
            "id",
            "party",
            "title",
            "event",
            "description",
            "date_start",
            "date_end",
        ]


class LanguageSerializer(ModelOwnerSerializer):
    """
    Languqage serializers
    """

    class Meta:
        model = Language
        fields = ["id", "party", "language", "talking", "writing", "comprehension"]


class WorkSampleSerializer(ModelOwnerSerializer):
    """
    Work Sample serializers
    """

    image = serializers.FileField(read_only=True)

    class Meta:
        model = WorkSample
        fields = ["id", "party", "title", "image", "skill", "description"]


class WorkSampleImageSerializer(ModelOwnerSerializer):
    """
    Work Sample Images serializers
    """

    class Meta:
        model = WorkSample
        fields = ["id", "image"]


class ExperienceSerializer(ModelOwnerSerializer):
    """
    Experience serializers
    """

    class Meta:
        model = Experience
        fields = [
            "id",
            "party",
            "title",
            "description",
            "place",
            "date_start",
            "date_end",
        ]


class SocialMediaSerializer(ModelOwnerSerializer):
    """
    Socials serializers
    """

    class Meta:
        model = SocialMedia
        fields = [
            "id",
            "party",
            "name",
            "userid",
            "phone",
            "link",
            "date_start",
            "date_end",
        ]


class AvatarSerializer(ModelOwnerSerializer):
    """
    Avatar serializers
    """

    class Meta:
        model = Profile
        fields = ["party", "avatar"]


class ProfileShortSerializer(ModelOwnerSerializer):
    """
    Short Profile serializers
    """

    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_user(self, obj):
        """
        Short Profile users  Get function
        """
        return UserSerializer(obj.party.user, context=self.context, many=False).data


class ProfileSerializer(ModelOwnerSerializer):
    """
    Profile serializers
    """

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
        """
        Contract Get function
        """
        qs = obj.party.party_contact.all()
        return ContactSerializer(qs, context=self.context, many=True).data

    def get_skills(self, obj):
        """
        Skills Get function
        """
        qs = obj.party.party_skill.all()
        return SkillSerializer(qs, context=self.context, many=True).data

    def get_jobs(self, obj):
        """
        Jobs Get function
        """
        qs = obj.party.party_job.all()
        return JobSerializer(qs, context=self.context, many=True).data

    def get_educations(self, obj):
        """
        Education Get function
        """
        qs = obj.party.party_education.all()
        return EducationSerializer(qs, context=self.context, many=True).data

    def get_certificates(self, obj):
        """
        Certificate Get function
        """
        qs = obj.party.party_certificate.all()
        return CertificateSerializer(qs, context=self.context, many=True).data

    def get_specialties(self, obj):
        """
        Specialties Get function
        """
        qs = obj.party.party_speciality.all()
        return SpecialtySerializer(qs, context=self.context, many=True).data

    def get_achievements(self, obj):
        """
        Achivments Get function
        """
        qs = obj.party.party_achievement.all()
        return AchievementSerializer(qs, context=self.context, many=True).data

    def get_languages(self, obj):
        """
        Language Get function
        """
        qs = obj.party.party_language.all()
        return LanguageSerializer(qs, context=self.context, many=True).data

    def get_work_samples(self, obj):
        """
        Work Get function
        """
        qs = obj.party.party_worksample.all()
        return WorkSampleSerializer(qs, context=self.context, many=True).data

    def get_experience(self, obj):
        """
        Experince Get function
        """
        qs = obj.party.party_experience.all()
        return ExperienceSerializer(qs, context=self.context, many=True).data

    def get_social_medias(self, obj):
        """
        Social Get function
        """
        qs = obj.party.party_socialmedia.all()
        return SocialMediaSerializer(qs, context=self.context, many=True).data

    def get_user(self, obj):
        """
        user Get function
        """
        return UserSerializer(obj.party.user, context=self.context, many=False).data
