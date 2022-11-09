import json
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters import rest_framework as filters
from library.permissions import IsOwnerOrReadOnly
from .serializers import PartySerializer, UserSerializer
from .serializers import ChangePasswordSerializer
from .serializers import UpdateUserSerializer
from .serializers import VoteSerializer
from .models import (Party,
                     Profile,
                     Vote)


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = PartySerializer


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email': user.email,
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('username',"party")
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
        return super().destroy(request, args, kwargs)

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    model = User
    permission_classes = (permissions.IsAuthenticated,)
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



class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = Vote
    permission_classes = [permissions.IsAuthenticated]

