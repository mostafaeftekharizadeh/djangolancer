import logging
from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .filters.profile import ProfileFilter
from rest_framework import status
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from .models import (Profile,
                     Skill,
                     Job,
                     Education,
                     Certificate,
                     Specialty,
                     Achievement,
                     Language,
                     WorkSample,
                     SocialMedia)

from .profile_serializers import (ProfileSerializer,
                          SkillSerializer,
                          JobSerializer,
                          EducationSerializer,
                          CertificateSerializer,
                          SpecialtySerializer,
                          AchievementSerializer,
                          LanguageSerializer,
                          WorkSampleSerializer,
                          SocialMediaSerializer)


_logger = logging.getLogger("midlancer.api.user.profile")

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.select_related('party__user')\
                .prefetch_related('party__party_skill')\
                .prefetch_related('party__party_job')\
                .prefetch_related('party__party_education')\
                .prefetch_related('party__party_certificate')\
                .prefetch_related('party__party_speciality')\
                .prefetch_related('party__party_achievement')\
                .prefetch_related('party__party_language')\
                .prefetch_related('party__party_worksample')\
                .prefetch_related('party__party_socialmedia')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProfileFilter
    logger = _logger

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class CertificateViewSet(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class SpecialtyViewSet(ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class AchievementViewSet(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class WorkSampleViewSet(ModelViewSet):
    queryset = WorkSample.objects.all()
    serializer_class = WorkSampleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

class SocialMediaViewSet(ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

