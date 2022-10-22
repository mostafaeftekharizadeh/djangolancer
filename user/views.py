import json
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import authentication, permissions
from .serializers import  UserSerializer
from .serializers import ChangePasswordSerializer
from .serializers import UpdateUserSerializer
from .serializers import ProfileSerializer,Profile_skillsSerializer,Profile_jobsSerializer,EducationSerializer
from .serializers import CertificateSerializer,SpecialtySerializer,AchievementSerializer,ProfileLanguageSerializer
from .serializers import WorkSampleSerializer,SocialMediaSerializer,VotingSerializer
from .models import Profile, Skill, Job, Education,Certificate,Specialty,Achievement,Language,WorkSample,SocialMedia,Voting



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(123)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email': user.email
        })

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

#class RefreshView(generics.CreateAPIView):
#    queryset = User.objects.all()
#    permission_classes = (permissions.AllowAny,)
#    serializer_class = UserRegisterSerializer
#    allowed_methods = ('GET',)
#    def get(self,  format=json):
#        return Response("{status:200}")
#
#class VerifyView(generics.CreateAPIView):
#    queryset = User.objects.all()
#    permission_classes = (permissions.AllowAny,)
#    serializer_class = UserRegisterSerializer
#    allowed_methods = ('GET',)
#    def get(self,  format=json):
#        return Response("{status:200}")
#
#class UserRegisterView(generics.CreateAPIView):
#    queryset = User.objects.all()
#    permission_classes = (permissions.AllowAny,)
#    serializer_class = UserRegisterSerializer
#
#class UpdateUserView(generics.UpdateAPIView):
#    queryset = User.objects.all()
#    model = User
#    permission_classes = (permissions.IsAuthenticated,)
#    serializer_class = UpdateUserSerializer
#
#    def get_object(self):
#        return self.request.user
#
class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    model = User
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class Profile_skillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = Profile_skillsSerializer
    permission_classes = [permissions.IsAuthenticated]

class Profile_jobsViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = Profile_jobsSerializer
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

class ProfileLanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = ProfileLanguageSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkSampleViewSet(viewsets.ModelViewSet):
    queryset = WorkSample.objects.all()
    serializer_class = WorkSampleSerializer
    permission_classes = [permissions.IsAuthenticated]

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [permissions.IsAuthenticated]

class VotingViewSet(viewsets.ModelViewSet):
    queryset = Voting.objects.all()
    serializer_class = Voting
    permission_classes = [permissions.IsAuthenticated]
