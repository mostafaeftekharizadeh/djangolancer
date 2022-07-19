from .models import Vacancy, Skill, Category, Level
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

class VacancySerializer(serializers.HyperlinkedModelSerializer):
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
                   'state',
                   'city']
