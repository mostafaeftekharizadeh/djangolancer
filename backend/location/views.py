import logging
from library.viewsets import ModelViewSet
from library.permissions import IsAdminOrReadOnly
from django.shortcuts import render
from .models import Place,Country,State,City
from .serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer

_logger = logging.getLogger('midlancer.api.location')

class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger

class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger
