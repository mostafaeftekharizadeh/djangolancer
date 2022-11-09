from rest_framework import serializers

class ModelOwnerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['party'] = self.context['request'].user.party
        return super().create(validated_data)
