from .models import Maintainer
from rest_framework import serializers

class MaintainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maintainer
        fields = ['name']
