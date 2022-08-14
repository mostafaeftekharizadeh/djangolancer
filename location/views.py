from rest_framework import viewsets
from rest_framework import authentication, permissions
from django.shortcuts import render
from .models import Place,Country,State,City
from .serializers import PlaceSerializer,CountrySerializer,StateSerializer,CitySerializer
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)