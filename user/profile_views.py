from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .filters.profile import ProfileFilter
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework import status
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


class ProfileViewSet(viewsets.ModelViewSet):
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

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class WorkSampleViewSet(viewsets.ModelViewSet):
    queryset = WorkSample.objects.all()
    serializer_class = WorkSampleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']

