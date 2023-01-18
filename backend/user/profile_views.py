"""
User Profile api endpoints module
"""
import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from .filters.profile import ProfileFilter
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

from .profile_serializers import (
    ProfileSerializer,
    AvatarSerializer,
    ContactSerializer,
    SkillSerializer,
    JobSerializer,
    EducationSerializer,
    CertificateSerializer,
    SpecialtySerializer,
    AchievementSerializer,
    LanguageSerializer,
    WorkSampleSerializer,
    WorkSampleImageSerializer,
    ExperienceSerializer,
    SocialMediaSerializer,
)

# pylint: disable=too-many-ancestors
_logger = logging.getLogger("midlancer.api.user.profile")


class ProfileViewSet(ModelViewSet):
    """
    Profile endpoint Viewset
    """

    queryset = (
        Profile.objects.select_related("party__user")
        .prefetch_related("party__party_skill")
        .prefetch_related("party__party_job")
        .prefetch_related("party__party_education")
        .prefetch_related("party__party_certificate")
        .prefetch_related("party__party_speciality")
        .prefetch_related("party__party_achievement")
        .prefetch_related("party__party_language")
        .prefetch_related("party__party_worksample")
        .prefetch_related("party__party_socialmedia")
    )
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProfileFilter
    logger = _logger

    def get_object(self):
        if self.kwargs["pk"] == "0":
            self.kwargs["pk"] = self.request.user.party.id
        return super().get_object()


class AvatarViewSet(ModelViewSet):
    """
    Avatar endpoint Viewset
    """

    queryset = Profile.objects.all()
    model = Profile
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AvatarSerializer
    parser_classes = (MultiPartParser,)
    http_method_names = ["put", "patch", "head", "delete"]

    def get_object(self):
        self.kwargs["pk"] = self.request.user.party.id
        return super().get_object()


class ContactViewSet(ModelViewSet):
    """
    Contact List endpoint Viewset
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger


class SkillViewSet(ModelViewSet):
    """
    Skill endpoint Viewset
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger


class JobViewSet(ModelViewSet):
    """
    Jobs endpoint Viewset
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger


class EducationViewSet(ModelViewSet):
    """
    Educations endpoint Viewset
    """

    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger


class CertificateViewSet(ModelViewSet):
    """
    User Certificates endpoint Viewset
    """

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger


class SpecialtyViewSet(ModelViewSet):
    """
    Specialty endpoint Viewset
    """

    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger


class AchievementViewSet(ModelViewSet):
    """
    Achivments endpoint Viewset
    """

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger


class LanguageViewSet(ModelViewSet):
    """
    Languages endpoint Viewset
    """

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger


class WorkSampleViewSet(ModelViewSet):
    """
    Work Sample endpoint Viewset
    """

    queryset = WorkSample.objects.all()
    serializer_class = WorkSampleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger


class WorkSampleImageViewSet(ModelViewSet):
    """
    Work Sample Images endpoint Viewset
    """

    queryset = WorkSample.objects.all()
    model = WorkSample
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WorkSampleImageSerializer
    parser_classes = (MultiPartParser,)
    http_method_names = ["head", "delete", "put", "patch"]


class ExperienceViewSet(ModelViewSet):
    """
    Experimence endpoint Viewset
    """

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger


class SocialMediaViewSet(ModelViewSet):
    """
    Social Media endpoint Viewset
    """

    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger
