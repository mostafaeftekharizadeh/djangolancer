from rest_framework import serializers

class ModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        if kwargs['context']['request'].method == "PATCH":
            kwargs['partial'] = True
        super(ModelSerializer, self).__init__(*args, **kwargs)

class ModelOwnerSerializer(ModelSerializer):
    # force party to be set to current user party id
    def to_internal_value(self, data):
        data['party'] = self.context['request'].user.party.id
        return super().to_internal_value(data)
