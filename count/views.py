from rest_framework import viewsets
from rest_framework import authentication, permissions
from configuration.serializers import  SkillSerializer, WorkCategorySerializer, LevelSerializer,EstimateSerializer
from location.serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer,PlaceSerializer
from configuration.models import Skill, WorkCategory,Level,Estimate
from location.models import Country,State,City,Place
from rest_framework import generics
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from .models import Count,Deposit,Withdraw,Account
from .serializers import CountSerializer,DepositSerializer,WithdrawSerializer,AccountSerializer
# Create your views here.
class CountViewSet(viewsets.ModelViewSet):
    queryset = Count.objects.all()
    serializer_class = CountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
class WithdrawViewSet(viewsets.ModelViewSet):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)