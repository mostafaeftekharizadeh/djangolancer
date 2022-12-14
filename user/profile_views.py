import logging
from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .filters.profile import ProfileFilter
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser
from .profile_models import (Profile,
                     Contact,
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
    def get_object(self):
        if self.kwargs['pk'] == "0":
            self.kwargs['pk']  = self.request.user.party.id
        return super(ProfileViewSet, self).get_object()


class AvatarView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    model = Profile
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AvatarSerializer
    parser_classes = (FormParser, MultiPartParser)
    def get_object(self):
        return self.request.user.party.party_profile

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']
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

