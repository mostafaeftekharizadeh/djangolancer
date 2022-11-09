from .models import (Estimate,
                     ProfileType,
                     Bank,
                     Language,
                     Level,
                     ViewStatus,
                     Currency,
                     Status,
                     Category,
                     Skill,
                     ComplainType,
                     Degree,
                     Category)
from rest_framework import serializers

class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields =  ['name','active']

class ProfileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileType
        fields =  ['name','active']

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name','active']

class BaseLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name','symbol','active']

class BaseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields =  ['name','active']

class ViewStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewStatus
        fields =  ['name','active']
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields =  ['name','active']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields =  ['name','active']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  ['name','active']

class BaseSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name','active']
class ComplainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplainType
        fields = ['name','active']
class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['name','active']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','type','parent','active']




