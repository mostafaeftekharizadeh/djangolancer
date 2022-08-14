from .models import Skill,WorkCategory,Level,Estimate
from rest_framework import serializers

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields =  ['name']
class WorkCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkCategory
        fields =  ['name']
class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields =  ['name']
class EstimateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estimate
        fields =  ['name']




