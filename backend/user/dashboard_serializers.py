"""
User Dashboard api Serializers
"""
import jdatetime
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from money.models import Transaction
from money.serializers import TransactionSerializer
from projects.models import Project,Offer
from projects.serializers import ProjectDetailSerializer,OfferSerializer

from .profile_models import Profile, Skill
from .user_serializers import UserSerializer


class SkillSerializer(ModelOwnerSerializer):
    """
    Skill Serializers
    """

    class Meta:
        model = Skill
        fields = ["id", "skill", "party", "level"]


class DashboardSerializer(ModelOwnerSerializer):
    """
    Dashboard Serializers
    """

    skills = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    my_projects = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    transactions = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()
    last_offer=serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_skills(self, obj):
        """
        Skill get Serializers
        """
        qs = obj.party.party_skill.all()
        return SkillSerializer(qs, context=self.context, many=True).data

    def get_my_projects(self, obj):
        """
        My projetcs get Serializers
        """
        qs = Project.objects.filter(party=obj.party)
        return ProjectDetailSerializer(qs, context=self.context, many=True).data
    
    def get_last_offer(self, obj):
        """
        Latest offer on projects
        """

        obj_offer=Offer.objects.filter(party=obj.party).latest('created_at')
        return OfferSerializer(obj_offer, context=self.context, many=False).data

    def get_projects(self, obj):
        """
        projetcs get Serializers
        """
        qs = Project.objects.filter(offers__party=obj.party)
        return ProjectDetailSerializer(qs, context=self.context, many=True).data

    def get_transactions(self, obj):
        """
        transaction get Serializers
        """
        qs = obj.party.wallet.all().first().transaction.all().order_by("-created_at")
        return TransactionSerializer(qs, context=self.context, many=True).data

    def get_payment(self, obj):
        """
        payment get Serializers
        """
        jtoday = jdatetime.datetime.now()
        last_month = jtoday.togregorian() - relativedelta(months=1)
        payment = {"pay": 0, "income": 0, "income_last_month": 0}
        pay = Transaction.objects.filter(
            wallet__party=obj.party, value__lt=0
        ).aggregate(Sum("value"))
        if pay['value__sum']:
            payment["pay"] = pay["value__sum"] * -1
        else:
            payment["pay"] = 0
        income = Transaction.objects.filter(
            wallet__party=obj.party, value__gt=0
        ).aggregate(Sum("value"))
        if income['value__sum']:
            payment["income"] = income["value__sum"]
        else:
            payment["income"] = 0
        income_last_month = Transaction.objects.filter(
            wallet__party=obj.party, value__gt=0, created_at__gt=last_month
        ).aggregate(Sum("value"))
        if income_last_month['value__sum']:
            payment["income_last_month"] = income_last_month["value__sum"]
        else:
            payment["income_last_month"] = 0
        return payment

    def get_user(self, obj):
        """
        user get Serializers
        """
        return UserSerializer(obj.party.user, context=self.context, many=False).data
