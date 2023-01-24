"""
Location App views
"""
import logging
from library.viewsets import ModelViewSet
from library.permissions import IsAdminOrReadOnly
from django.shortcuts import render
from .models import Place, Country, State, City
from .serializers import (
    PlaceSerializer,
    CountrySerializer,
    StateSerializer,
    CitySerializer,
)

_logger = logging.getLogger("midlancer.api.location")


class PlaceViewSet(ModelViewSet):
    """
    Location Place views
    """

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class CountryViewSet(ModelViewSet):
    """
    Location Country views
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class StateViewSet(ModelViewSet):
    """
    Location State views
    """

    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class CityViewSet(ModelViewSet):
    """
    Location City views
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger
