from rest_framework import serializers

class ModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        try:
            # force partial update on PATCH request
            if kwargs['context']['request'].method in ["PATCH", "DELETE"]:
                kwargs['partial'] = True
        except:
            pass
        super(ModelSerializer, self).__init__(*args, **kwargs)

class ModelOwnerSerializer(ModelSerializer):
    # force party to be set to current user party id
    def to_internal_value(self, data):
        _mutable = data._mutable
        data._mutable = True
        data['party'] = self.context['request'].user.party.id
        data._mutable = _mutable
        return super().to_internal_value(data)
