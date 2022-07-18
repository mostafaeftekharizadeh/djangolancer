from .models import Vacancy
from rest_framework import serializers

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
