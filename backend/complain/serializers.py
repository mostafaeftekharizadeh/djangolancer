"""
Complain Serializer
"""
from rest_framework import serializers
from .models import Complain, ResultComplain


class ComplainSerializer(serializers.HyperlinkedModelSerializer):
    """
    Complain Serializer
    """

    class Meta:
        model = Complain
        fields = ["description"]


class ResultComplainSerializer(serializers.HyperlinkedModelSerializer):
    """
    ResultComplain Serializer
    """

    class Meta:
        model = ResultComplain
        fields = ["description"]
