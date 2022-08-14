from rest_framework import viewsets
from rest_framework import authentication, permissions
from .serializers import ProjectSerializer
from configuration.serializers import  SkillSerializer, WorkCategorySerializer, LevelSerializer,EstimateSerializer
from location.serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer
from .models import Profile,Project
from configuration.models import Skill, WorkCategory,Level,Estimate
from location.models import Country,State,City,Place
from rest_framework import generics
from django_filters import rest_framework as filters
from django.contrib.auth.models import User

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('country', 'state', 'city', 'skills', 'user', 'level', 'place')
    
    '''
    filter projects based on owner
    '''
    def get_queryset(self):
        if self.request.GET.get('owner') == '1':
            return Project.objects.filter(user=self.request.user)
        else:
            return Project.objects.all().exclude(user=self.request.user)

