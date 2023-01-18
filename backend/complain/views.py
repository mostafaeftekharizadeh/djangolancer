import logging
from rest_framework import viewsets
from rest_framework import authentication, permissions
from location.serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer,PlaceSerializer
from location.models import Country,State,City,Place
from rest_framework import generics
from django_filters import rest_framework as filters
from django.contrib.auth.models import User

from .models import Complain,ResultComplain
from .serializers import ComplainSerializer,ResultComplainSerializer
from library.viewsets import ModelViewSet

_logger = logging.getLogger('midlancer.api.complain')


class ComplainViewSet(ModelViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
    logger = _logger

class ResultComplainViewSet(ModelViewSet):
    queryset = ResultComplain.objects.all()
    serializer_class = ResultComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
    logger = _logger
