from .models import Vacancy, Skill, Category,Place, Level, Country,State,City,Estimate
from rest_framework import serializers

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields =  ['name']
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields =  ['name']
class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields =  ['name']
class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields =  ['name']
class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields =  ['name']
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields =  ['name']
class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields =  ['name']

class EstimateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estimate
        fields =  ['name']

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields =  ['title',
                   'category',
                   'level',
                   'time_estimate',
                   'place',
                   'expire_date',
                   'budget_total',
                   'budget_min', 'budget_max',
                   'deposit',
                   'description',
                   'skills',
                   'country',
                   'state',
                   'city',
                   'status']
        ordering_fields = ['title']
        nested_depth = 2
