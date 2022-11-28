from .models import Country,State,City,Place
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields =  ['name','initials','code','active']
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields =  ['name','initials','code','country','active']
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields =  ['name','state','active']
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields =  ['name','active']




