from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .filters.profile import ProfileFilter
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework import status
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
from .serializers import (ProfileSerializer,
                          SkillSerializer,
                          JobsSerializer,
                          EducationSerializer,
                          CertificateSerializer,
                          SpecialtySerializer,
                          AchievementSerializer,
                          LanguageSerializer,
                          WorkSampleSerializer,
                          SocialMediaSerializer)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProfileFilter
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_authenticated == False or instance.party.user != request.user:
            return Response({'error': "Permission Denied"}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, args, kwargs)

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [permissions.IsAuthenticated]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [permissions.IsAuthenticated]

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticated]

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkSampleViewSet(viewsets.ModelViewSet):
    queryset = WorkSample.objects.all()
    serializer_class = WorkSampleSerializer
    permission_classes = [permissions.IsAuthenticated]

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [permissions.IsAuthenticated]

