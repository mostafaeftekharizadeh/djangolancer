from rest_framework import viewsets
from rest_framework import authentication, permissions
from configuration.serializers import  SkillSerializer, WorkCategorySerializer, LevelSerializer,EstimateSerializer
from location.serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer,PlaceSerializer
from configuration.models import Skill, WorkCategory,Level,Estimate
from location.models import Country,State,City,Place
from rest_framework import generics
from django_filters import rest_framework as filters
from django.contrib.auth.models import User

from .models import Complain,ResultComplain
from .serializers import ComplainSerializer,ResultComplainSerializer

# Create your views here.
class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)

class ResultComplainViewSet(viewsets.ModelViewSet):
    queryset = ResultComplain.objects.all()
    serializer_class = ResultComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)