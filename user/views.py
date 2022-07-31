from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import authentication, permissions
from .serializers import MaintainerSerializer, UserRegisterSerializer
from .models import Maintainer



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
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

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer

class MaintainerViewSet(viewsets.ModelViewSet):
    queryset = Maintainer.objects.all()
    serializer_class = MaintainerSerializer
    permission_classes = [permissions.IsAuthenticated]
