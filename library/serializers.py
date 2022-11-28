from rest_framework import serializers

class ModelOwnerSerializer(serializers.ModelSerializer):
    # force object party to be set to current user party id
    def to_internal_value(self, data):
        data['party'] = self.context['request'].user.party.id
        return super().to_internal_value(data)
