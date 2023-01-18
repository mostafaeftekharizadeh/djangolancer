from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from .models import Wallet, Transaction, CardTransfer

class CardTransferSerializer(ModelOwnerSerializer):
    state = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    transfered_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = CardTransfer
        fields = ['id', 'party', 'number', 'shaba', 'value', 'state', 'created_at', 'transfered_at']
    def create(self, validated_data):
        obj = super().create(validated_data)
        if obj.created_at == None:
            raise serializers.ValidationError({'non_field_errors' :'cant transfer!'})
        return obj

class WalletSerializer(ModelOwnerSerializer):
    target = serializers.UUIDField(write_only=True, required=False)
    class Meta:
        model = Wallet
        fields = ['id', 'party', 'balance', 'target']

class TransactionSerializer(ModelOwnerSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

