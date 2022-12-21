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
        qs = obj.offerstep_set.all()
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
