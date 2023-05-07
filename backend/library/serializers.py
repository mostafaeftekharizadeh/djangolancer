"""
Library Base Serializer
"""
from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):
    """
    Library Model Serializer
    """

    def __init__(self, *args, **kwargs):
        try:
            # force partial update on PATCH request
            if kwargs["context"]["request"].method in ["PATCH", "DELETE"]:
                kwargs["partial"] = True
        except:
            pass
        super(ModelSerializer, self).__init__(*args, **kwargs)


class ModelOwnerSerializer(ModelSerializer):
    """
    Library Owner Serializer
    """

    def to_internal_value(self, data):
        """
        force party to be set to current user party id
        """
        _mutable = False
        try:
            _mutable = data._mutable
            data._mutable = True
        except:
            pass
        data["party"] = self.context["request"].user.party.id
        try:
            data._mutable = _mutable
        except:
            pass
        return super().to_internal_value(data)
