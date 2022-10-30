from .models import Estimate,ProfileType,BankName,Language,Level,ViewStatus,Currency,Status,Category,Skill,ComplainType,Degree,Category
from rest_framework import serializers

class EstimateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estimate
        fields =  ['name','active']

class ProfileTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProfileType
        fields =  ['name','active']

class BankNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankName
        fields = ['name','active']

class BaseLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['name','symbol','active']

class BaseLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields =  ['name','active']

class ViewStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ViewStatus
        fields =  ['name','active']
class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields =  ['name','active']

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields =  ['name','active']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields =  ['name','active']

class BaseSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['name','active']
class ComplainTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComplainType
        fields = ['name','active']
class DegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degree
        fields = ['name','active']
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name','type','parent','active']




