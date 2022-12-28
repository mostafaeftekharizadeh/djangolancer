import logging
import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework import serializers, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters import rest_framework as filters
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from library.throttle import OTPMinuteRateThrottle, OTPHourRateThrottle
from .user_serializers import  (UserSerializer,
                                AuthTokenSerializer,
                                OtpSerializer,
                                PartySerializer,
                                ChangePasswordSerializer,
                                #UpdateUserSerializer,
                                VoteSerializer)
from .profile_serializers import ProfileSerializer
from .user_models import Otp
from .profile_models import (Party,
                     Profile,
                     Vote)

User = get_user_model()
_logger = logging.getLogger('midlancer.api.user.user')

class OtpViewSet(ModelViewSet):
    queryset = Otp.objects.all()
    serializer_class = OtpSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['post']
    throttle_classes = [OTPMinuteRateThrottle, OTPHourRateThrottle]


class PartyViewSet(ModelViewSet):
    queryset = Party.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = PartySerializer
    logger = _logger

#class LoginView(ObtainAuthToken):
class LoginView(generics.CreateAPIView):
    serializer_class = AuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if not serializer.is_valid(raise_exception=False):
            if 'password' in request.data:
                request.data['password'] = "**********"
            _logger.error('Login failed {}'.format(request.data))
            raise serializers.ValidationError(serializer.errors)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'id' : user.id,
            'token': token.key,
            'profile' : None,
            'party' : None
        }
        if hasattr(user, 'party'):
            data['party'] = user.party.id
            profile = ProfileSerializer(Profile.objects.filter(party=user.party), context={'request': request}, many=True).data
            if len(profile) > 0:
                data['profile'] = profile[0]
        username = user.username if user else '<none>'
        if 'password' in request.data:
            request.data['password'] = "**********"
        _logger.info('Loged in {}.'.format(request.data))
        return Response(data)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('mobile',"party")
    logger = _logger
    throttle_classes = [OTPMinuteRateThrottle, OTPHourRateThrottle]
    #def list(self, request, *args, **kwargs):
        #if request.user.is_authenticated == False:
        #    return Response({'error': "Permission Denied"}, status=status.HTTP_400_BAD_REQUEST)
    #    return super().list(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_authenticated == False or instance != request.user:
            return Response({'error': "Permission Denied"}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_authenticated == False or instance != request.user:
            return Response({'error': "Permission Denied"}, status=status.HTTP_400_BAD_REQUEST)
        instance.is_active = False
        instance.save()

        return super().update(request, args, kwargs)

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChangePasswordSerializer
    def get_object(self):
        return self.request.user



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



class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = Vote
    permission_classes = [permissions.IsAuthenticated]
    logger = _logger

