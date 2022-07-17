from django.shortcuts import render
from django.contrib.auth import views as auth_views
from rest_framework import viewsets
from rest_framework import authentication, permissions
from .serializers import MaintainerSerializer
from .models import Maintainer



class LoginView(auth_views.LoginView):
    def post(self, request, *args, **kwargs):
        ret = super(LoginView, self).post(request, *args, **kwargs)
        print(ret)

class MaintainerViewSet(viewsets.ModelViewSet):
    queryset = Maintainer.objects.all()
    serializer_class = MaintainerSerializer
    permission_classes = [permissions.IsAuthenticated]
