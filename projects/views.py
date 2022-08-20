from rest_framework import viewsets
from rest_framework import authentication, permissions
from .serializers import ProjectSerializer,FileSerializer,CostSerializer,OfferSerializer,OfferLevelSerializer,BudgetSerializer
from configuration.serializers import  SkillSerializer, WorkCategorySerializer, LevelSerializer,EstimateSerializer
from location.serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer,PlaceSerializer
from .models import Profile,Project,File,Cost,Offer,OfferLevel,Budget
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

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('project')

class CostViewSet(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
class OfferLevelViewSet(viewsets.ModelViewSet):
    queryset = OfferLevel.objects.all()
    serializer_class = OfferLevelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)