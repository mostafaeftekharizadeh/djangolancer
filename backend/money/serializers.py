"""
Money serializer
"""
import jdatetime
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from .models import Wallet, Transaction, CardTransfer


class CardTransferSerializer(ModelOwnerSerializer):
    """
    Card Transfer serializer
    """

    state = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    transfered_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CardTransfer
        fields = [
            "id",
            "party",
            "number",
            "shaba",
            "value",
            "state",
            "tracking_code",
            "created_at",
            "transfered_at",
        ]

    def create(self, validated_data):
        obj = super().create(validated_data)
        print(obj.created_at)
        if obj.created_at is None:
            raise serializers.ValidationError({"non_field_errors": "cant transfer!"})
        return obj


class WalletSerializer(ModelOwnerSerializer):
    """
    Wallet serializer
    """

    target = serializers.UUIDField(write_only=True, required=False)
    payment = serializers.SerializerMethodField()

    def get_payment(self, obj):
        """
        payment get Serializers
        """
        jtoday = jdatetime.datetime.now()
        last_month = jtoday.togregorian() - relativedelta(months=1)
        payment = {"income": 0, "income_last_month": 0}
        # income = Transaction.objects.filter(
        #     wallet__party=obj.party, value__gt=0
        # ).aggregate(Sum("value"))

        payment["income"] = obj.balance

        income_last_month = Transaction.objects.filter(
            wallet__party=obj.party, value__gt=0, created_at__gt=last_month
        ).aggregate(Sum("value"))
        if income_last_month["value__sum"]:
            payment["income_last_month"] = income_last_month["value__sum"]
        else:
            payment["income_last_month"] = 0
        return payment

    class Meta:
        model = Wallet
        fields = ["id", "party", "balance", "target", "payment"]


class TransactionSerializer(ModelOwnerSerializer):
    """
    Transaction serializer
    """

    class Meta:
        model = Transaction
        fields = "__all__"
