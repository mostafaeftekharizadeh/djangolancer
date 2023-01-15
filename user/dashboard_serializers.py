from django.db.models import Sum
import jdatetime
from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from .user_serializers import UserSerializer, PartySerializer
from .profile_models import  Profile, Skill
from projects.models import Project
from projects.serializers import ProjectSerializer, ProjectDetailSerializer
from money.serializers import TransactionSerializer
from money.models import Transaction



class SkillSerializer(ModelOwnerSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill', 'party', 'level']

class DashboardSerializer(ModelOwnerSerializer):
    skills = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    my_projects = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    transactions = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = "__all__"
    def get_skills(self, obj):
        qs = obj.party.party_skill.all()
        return SkillSerializer(qs, context=self.context, many=True).data
    def get_my_projects(self, obj):
        qs = Project.objects.filter(party=obj.party)
        return ProjectDetailSerializer(qs, context=self.context, many=True).data
    def get_projects(self, obj):
        qs = Project.objects.filter(offers__party=obj.party)
        return ProjectDetailSerializer(qs, context=self.context, many=True).data
    def get_transactions(self, obj):
        qs = obj.party.wallet.all().first().transaction.all().order_by('-created_at')
        return TransactionSerializer(qs, context=self.context, many=True).data
    def get_payment(self, obj):
        jtoday = jdatetime.datetime.now()
        last_month = jtoday.togregorian() - relativedelta(months=1)
        payment = {
            "pay" : 0,
            "income" : 0,
            "income_last_month": 0
        }
        pay = Transaction.objects.filter(wallet__party=obj.party, value__lt=0).aggregate(Sum('value'))
        payment['pay'] = pay['value__sum'] * -1
        income = Transaction.objects.filter(wallet__party=obj.party, value__gt=0).aggregate(Sum('value'))
        payment['income'] = income['value__sum']
        income_last_month = Transaction.objects.filter(wallet__party=obj.party,
                                                       value__gt=0,
                                                       created_at__gt=last_month).aggregate(Sum('value'))
        payment['income_last_month'] = income_last_month['value__sum']
        return payment
    def get_user(self, obj):
        return UserSerializer(obj.party.user, context=self.context, many=False).data
