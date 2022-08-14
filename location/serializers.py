from .models import Country,State,City,Place
from rest_framework import serializers

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields =  ['name','active']
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields =  ['name','active']
class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields =  ['name','active']
class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields =  ['name','active']




