from .models import Complain,ResultComplain
from rest_framework import serializers

class ComplainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complain
        fields =  ['description']
class ResultComplainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResultComplain
        fields =  ['description']
