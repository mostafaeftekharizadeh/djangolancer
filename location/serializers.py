from .models import Country,State,City,Place
from rest_framework import serializers

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields =  ['name','initials','code','active']
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields =  ['name','initials','code','country','active']
class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields =  ['name','state','active']
class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields =  ['name','active']




