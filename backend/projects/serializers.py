"""
Project Serializers
"""
from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from user.user_serializers import UserSerializer
from .models import Project, File, Cost, Offer, OfferStep, Budget

# pylint: disable=too-many-ancestors
class ProjectSerializer(ModelOwnerSerializer):
    """
    Project Serializer
    """

    user = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
        fields = [
            "id",
            "party",
            "category",
            "sub_category",
            "title",
            "description",
            "skill",
            "duration",
            "level",
            "budget_min",
            "budget_max",
            "status",
            "user",
        ]
        ordering_fields = ["title"]
        extra_kwargs = {
            'status': {'read_only': True},
        }

    def get_user(self, obj):
        """
        Project get Serializer
        """
        return UserSerializer(obj.party.user, context=self.context, many=False).data


class ProjectDetailSerializer(ModelOwnerSerializer):
    """
    Project detaile Serializer
    """

    user = serializers.SerializerMethodField()
    offer = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
        fields = [
            "id",
            "party",
            "category",
            "sub_category",
            "title",
            "description",
            "skill",
            "duration",
            "level",
            "budget_min",
            "budget_max",
            "status",
            "offer",
            "messages",
            "user",
        ]
        ordering_fields = ["title"]
        extra_kwargs = {
            'status': {'read_only': True},
        }

    def get_offer(self, obj):
        """
        Project get offers serializer function
        """
        qs = obj.offers.filter(state="a")
        return OfferSerializer(qs, context=self.context, many=True).data

    def get_messages(self, obj):
        """
        Project get messages serializer function
        """
        count = 0
        offer = obj.offers.filter(state="a").first()
        if offer:
            room = obj.room.filter(chat_participate__party=offer.party).first()
            if room:
                count = room.target.all().count()
        return count

    def get_user(self, obj):
        """
        Project get users serializer function
        """
        return UserSerializer(obj.party.user, context=self.context, many=False).data


class FileSerializer(ModelOwnerSerializer):
    """
    Project files serializer
    """

    class Meta:
        model = File
        fields = ["party", "project", "project_file"]

    def validate(self, attrs):
        if attrs["project"].party != self.context["request"].user.party:
            raise serializers.ValidationError("permission denied.")
        # return super(FileSerializer, self).validate(attrs)
        return super().validate(attrs)


class CostSerializer(serializers.ModelSerializer):
    """
    Project's cost serializer
    """

    class Meta:
        model = Cost
        fields = ["project", "calculate_cost", "pay_cost", "pay_date"]
        # ordering_fields = ['title']
        # nested_depth = 2


class OfferSerializer(ModelOwnerSerializer):
    """
    Project offer serializer
    """

    offersteps = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = "__all__"

    def get_offersteps(self, obj):
        """
        Project get offer serializer
        """
        qs = obj.offersteps.all()
        return OfferStepSerializer(qs, context=self.context, many=True).data

    def create(self, validated_data):
        offer = super().create(validated_data)
        offer_step = OfferStep(
            offer=offer,
            party=offer.party,
            duration=offer.duration,
            title=offer.title,
            cost=offer.cost,
        )
        offer_step.save()
        return offer


class OfferStepSerializer(serializers.ModelSerializer):
    """
    Project offer steps serializer
    """

    class Meta:
        model = OfferStep
        fields = "__all__"


class BudgetSerializer(serializers.ModelSerializer):
    """
    Project budget serializer
    """

    class Meta:
        model = Budget
        fields = ["project", "currency", "title", "time", "optional", "cost"]
        ordering_fields = ["title"]
        nested_depth = 2
