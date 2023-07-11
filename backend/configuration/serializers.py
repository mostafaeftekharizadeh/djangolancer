"""
Configuration Serializer
"""
from django.contrib.sites.models import Site
from rest_framework import serializers
from .models import (
    Estimate,
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
    Category,
)


# pylint: disable=too-many-ancestors
class EstimateSerializer(serializers.ModelSerializer):
    """
    Estimate serializer
    """

    class Meta:
        model = Estimate
        fields = ["id", "name", "active"]


class ProfileTypeSerializer(serializers.ModelSerializer):
    """
    Profile type serializer
    """

    class Meta:
        model = ProfileType
        fields = ["id", "name", "active"]


class BankSerializer(serializers.ModelSerializer):
    """
    Bank serializer
    """

    class Meta:
        model = Bank
        fields = ["id", "name", "active"]


class BaseLanguageSerializer(serializers.ModelSerializer):
    """
    Base Language serializer
    """

    class Meta:
        model = Language
        fields = ["name", "symbol", "active"]


class BaseLevelSerializer(serializers.ModelSerializer):
    """
    Base Level serializer
    """

    class Meta:
        model = Level
        fields = ["id", "name", "active"]


class ViewStatusSerializer(serializers.ModelSerializer):
    """
    View Status serializer
    """

    class Meta:
        model = ViewStatus
        fields = ["id", "name", "active"]


class CurrencySerializer(serializers.ModelSerializer):
    """
    Currency serializer
    """

    class Meta:
        model = Currency
        fields = ["id", "name", "active"]


class StatusSerializer(serializers.ModelSerializer):
    """
    Status serializer
    """

    class Meta:
        model = Status
        fields = ["id", "name", "active"]


class BaseSkillSerializer(serializers.ModelSerializer):
    """
    Base Skill serializer
    """

    class Meta:
        model = Skill
        fields = ["id", "name", "active", "category"]


class ComplainTypeSerializer(serializers.ModelSerializer):
    """
    Complain serializer
    """

    class Meta:
        model = ComplainType
        fields = ["id", "name", "active"]


class DegreeSerializer(serializers.ModelSerializer):
    """
    Degree serializer
    """

    class Meta:
        model = Degree
        fields = ["id", "name", "active"]


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer
    """

    class Meta:
        model = Category
        fields = ["id", "name", "type", "parent", "active"]


class SiteSerializer(serializers.ModelSerializer):
    """
    Site serializer
    """

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
        fields = "__all__"

    def get_estimate(self, obj):
        """
        Site estimate serializer
        """
        qs = Estimate.objects.filter(active=True)
        return EstimateSerializer(qs, context=self.context, many=True).data

    def get_profile_type(self, obj):
        """
        Site profile type serializer
        """
        qs = ProfileType.objects.filter(active=True)
        return ProfileTypeSerializer(qs, context=self.context, many=True).data

    def get_bank(self, obj):
        """
        Site bank serializer
        """
        qs = Bank.objects.filter(active=True)
        return BankSerializer(qs, context=self.context, many=True).data

    def get_language(self, obj):
        """
        Site language serializer
        """
        qs = Language.objects.filter(active=True)
        return BaseLanguageSerializer(qs, context=self.context, many=True).data

    def get_level(self, obj):
        """
        Site Level serializer
        """
        qs = Level.objects.filter(active=True)
        return BaseLevelSerializer(qs, context=self.context, many=True).data

    def get_currency(self, obj):
        """
        Site estimate serializer
        """
        qs = Currency.objects.filter(active=True)
        return CurrencySerializer(qs, context=self.context, many=True).data

    def get_status(self, obj):
        """
        site status serializer
        """
        qs = Status.objects.filter(active=True)
        return StatusSerializer(qs, context=self.context, many=True).data

    def get_skill(self, obj):
        """
        Site skill serializer
        """
        qs = Skill.objects.filter(active=True)
        return BaseSkillSerializer(qs, context=self.context, many=True).data

    def get_complain_type(self, obj):
        """
        Site complain type serializer
        """
        qs = ComplainType.objects.filter(active=True)
        return ComplainTypeSerializer(qs, context=self.context, many=True).data

    def get_degree(self, obj):
        """
        Site degree serializer
        """
        qs = Degree.objects.filter(active=True)
        return DegreeSerializer(qs, context=self.context, many=True).data

    def get_category(self, obj):
        """
        Site category serializer
        """
        qs = Category.objects.filter(active=True)
        return CategorySerializer(qs, context=self.context, many=True).data
