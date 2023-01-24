"""
Location Serializers
"""
from rest_framework import serializers
from .models import Country, State, City, Place


class CountrySerializer(serializers.ModelSerializer):
    """
    Country Serializers
    """

    class Meta:
        model = Country
        fields = ["name", "initials", "code", "active"]


class StateSerializer(serializers.ModelSerializer):
    """
    State Serializers
    """

    class Meta:
        model = State
        fields = ["name", "initials", "code", "country", "active"]


class CitySerializer(serializers.ModelSerializer):
    """
    City Serializers
    """

    class Meta:
        model = City
        fields = ["name", "state", "active"]


class PlaceSerializer(serializers.ModelSerializer):
    """
    Place Serializers
    """

    class Meta:
        model = Place
        fields = ["name", "active"]
