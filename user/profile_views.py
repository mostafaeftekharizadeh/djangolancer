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


    def create(self, request, *args, **kwargs):
        request.data['party']=request.user.party.id
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        request.data['party']=request.user.party.id
        instance = self.get_object()
        if request.user.is_authenticated == False or instance.party.user != request.user:
            self.permission_denied(request,  message="Permission Denied", code=status.HTTP_400_BAD_REQUEST)
        return super().update(request, args, kwargs)

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(party=self.request.user.party)

    def check_object_permissions(self, request, obj):
        if obj.party != request.user.party:
            self.permission_denied(request,  message="Permission Denied", code=status.HTTP_400_BAD_REQUEST)
        return super().check_object_permissions(request, obj)

    def perform_create(self, serializer):
        serializer.save(party=self.request.user.party)



class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(party=self.request.user.party)

    def check_object_permissions(self, request, obj):
        if obj.party != request.user.party:
            self.permission_denied(request,  message="Permission Denied", code=status.HTTP_400_BAD_REQUEST)
        return super().check_object_permissions(request, obj)

    def perform_create(self, serializer):
        serializer.save(party=self.request.user.party)

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(party=self.request.user.party)

    def check_object_permissions(self, request, obj):
        if obj.party != request.user.party:
            self.permission_denied(request,  message="Permission Denied", code=status.HTTP_400_BAD_REQUEST)
        return super().check_object_permissions(request, obj)

    def perform_create(self, serializer):
        serializer.save(party=self.request.user.party)

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(party=self.request.user.party)

    def check_object_permissions(self, request, obj):
        if obj.party != request.user.party:
            self.permission_denied(request,  message="Permission Denied", code=status.HTTP_400_BAD_REQUEST)
        return super().check_object_permissions(request, obj)

    def perform_create(self, serializer):
        serializer.save(party=self.request.user.party)

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(party=self.request.user.party)

    def check_object_permissions(self, request, obj):
        if obj.party != request.user.party:
            self.permission_denied(request,  message="Permission Denied", code=status.HTTP_400_BAD_REQUEST)
        return super().check_object_permissions(request, obj)

    def perform_create(self, serializer):
        serializer.save(party=self.request.user.party)

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

