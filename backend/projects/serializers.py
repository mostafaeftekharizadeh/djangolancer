from rest_framework import serializers
from .models import (Project,
                     File,
                     Cost,
                     Offer,
                     OfferStep,
                     Budget)
from library.serializers import ModelOwnerSerializer
from user.user_serializers import UserSerializer
from configuration.serializers import BaseSkillSerializer


class ProjectSerializer(ModelOwnerSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'
        fields = ['id',
                  'party',
                  'category',
                  'sub_category',
                  'title',
                  'description',
                  'skill',
                  'level',
                  'budget_min',
                  'budget_max',
                  'user',
                  ]
        ordering_fields = ['title']
    def get_user(self, obj):
        return UserSerializer(obj.party.user, context=self.context, many=False).data

class ProjectDetailSerializer(ModelOwnerSerializer):
    user = serializers.SerializerMethodField()
    offer = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'
        fields = ['id',
                  'party',
                  'category',
                  'sub_category',
                  'title',
                  'description',
                  'skill',
                  'level',
                  'budget_min',
                  'budget_max',
                  'offer',
                  'messages',
                  'user',
                  ]
        ordering_fields = ['title']
    def get_offer(self, obj):
        qs = obj.offers.filter(state='a')
        return OfferSerializer(qs, context=self.context, many=True).data
    def get_messages(self, obj):
        count = 0
        offer = obj.offers.filter(state='a').first()
        if offer:
            room = obj.room.filter(chat_participate__party=offer.party).first()
            if room:
                count = room.target.all().count()
        return count
    def get_user(self, obj):
        return UserSerializer(obj.party.user, context=self.context, many=False).data


class FileSerializer(ModelOwnerSerializer):
    class Meta:
        model = File
        fields =  ['party', 'project', 'project_file']
    def validate(self, attrs):
        if attrs['project'].party != self.context['request'].user.party:
            raise serializers.ValidationError('permission denied.')
        return super(FileSerializer, self).validate(attrs)

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields =  ['project',
                    'calculate_cost',
                    'pay_cost',
                    'pay_date'
                    ]
        # ordering_fields = ['title']
        # nested_depth = 2

class OfferSerializer(ModelOwnerSerializer):
    offersteps = serializers.SerializerMethodField()
    class Meta:
        model = Offer
        fields =  "__all__"
    def get_offersteps(self, obj):
        qs = obj.offersteps.all()
        return OfferStepSerializer(qs, context=self.context, many=True).data

    def create(self, validated_data):
        offer = super().create(validated_data)
        offerStep = OfferStep(
            offer=offer,
            party=offer.party,
            duration=offer.duration,
            title=offer.title,
            cost=offer.cost
        )
        offerStep.save()
        return offer


class OfferStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferStep
        fields =  "__all__"

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields =  ['project',
                    'currency',
                    'title',
                    'time',
                    'optional',
                    'cost'
                    ]
        ordering_fields = ['title']
        nested_depth = 2
