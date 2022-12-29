from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from .models import Wallet, Transaction

class WalletSerializer(ModelOwnerSerializer):
    target = serializers.UUIDField(write_only=True, required=False)
    class Meta:
        model = Wallet
        fields = ['id', 'party', 'balance', 'target']

class TransactionSerializer(ModelOwnerSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

