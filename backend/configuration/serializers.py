from django.contrib.sites.models import Site
from .models import (Estimate,
                     ProfileType,
                     Bank,
                     Language,
                     Level,
                     ViewStatus,
                     Currency,
                     Status,
                     Skill,
                     ComplainType,
                     Degree,
                     Category)
from rest_framework import serializers

class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields =  ['id', 'name', 'active']

class ProfileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileType
        fields =  ['id', 'name', 'active']

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'active']

class BaseLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name','symbol', 'active']

class BaseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields =  ['id', 'name', 'active']

class ViewStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewStatus
        fields =  ['id', 'name', 'active']
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields =  ['id', 'name', 'active']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields =  ['id', 'name', 'active']

class BaseSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'active']

class ComplainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplainType
        fields = ['id', 'name', 'active']

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['id', 'name', 'active']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'parent', 'active']

class SiteSerializer(serializers.ModelSerializer):
    estimate = serializers.SerializerMethodField()
    profile_type = serializers.SerializerMethodField()
    bank = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()
    complain_type = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Site
        fields = '__all__'
    def get_estimate(self, obj):
        qs = Estimate.objects.filter(active=True)
        return EstimateSerializer(qs, context=self.context, many=True).data
    def get_profile_type(self, obj):
        qs = ProfileType.objects.filter(active=True)
        return ProfileTypeSerializer(qs, context=self.context, many=True).data
    def get_bank(self, obj):
        qs = Bank.objects.filter(active=True)
        return BankSerializer(qs, context=self.context, many=True).data
    def get_language(self, obj):
        qs = Language.objects.filter(active=True)
        return BaseLanguageSerializer(qs, context=self.context, many=True).data
    def get_level(self, obj):
        qs = Level.objects.filter(active=True)
        return BaseLevelSerializer(qs, context=self.context, many=True).data
    def get_currency(self, obj):
        qs = Currency.objects.filter(active=True)
        return CurrencySerializer(qs, context=self.context, many=True).data
    def get_status(self, obj):
        qs = Status.objects.filter(active=True)
        return StatusSerializer(qs, context=self.context, many=True).data
    def get_skill(self, obj):
        qs = Skill.objects.filter(active=True)
        return BaseSkillSerializer(qs, context=self.context, many=True).data
    def get_complain_type(self, obj):
        qs = ComplainType.objects.filter(active=True)
        return ComplainTypeSerializer(qs, context=self.context, many=True).data
    def get_degree(self, obj):
        qs = Degree.objects.filter(active=True)
        return DegreeSerializer(qs, context=self.context, many=True).data
    def get_category(self, obj):
        qs = Category.objects.filter(active=True)
        return CategorySerializer(qs, context=self.context, many=True).data


