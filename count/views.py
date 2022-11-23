import logging
from rest_framework import viewsets
from rest_framework import authentication, permissions
from location.serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer,PlaceSerializer
from location.models import Country,State,City,Place
from rest_framework import generics
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from .models import Count,Deposit,Withdraw,Account
from .serializers import CountSerializer,DepositSerializer,WithdrawSerializer,AccountSerializer
from library.viewsets import ModelViewSet

_logger = logging.getLogger('midlancer.api.count')


class CountViewSet(ModelViewSet):
    queryset = Count.objects.all()
    serializer_class = CountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    logger = _logger

class DepositViewSet(ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    logger = _logger

class WithdrawViewSet(ModelViewSet):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    logger = _logger

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
