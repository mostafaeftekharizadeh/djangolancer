from rest_framework import serializers
from .models import Project,File,Cost,Offer,OfferLevel,Budget
from library.serializers import ModelOwnerSerializer
from user.user_serializers import UserSerializer




class ProjectSerializer(ModelOwnerSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'
        ordering_fields = ['title']
        nested_depth = 2
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
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields =  ['project',
                    # 'profile',
                    'total_level',
                    'total_time',
                    'total_price',
                    'promotion',
                    'description',
                    'state'
                    ]
        ordering_fields = ['total_price']
        nested_depth = 2
class OfferLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferLevel
        fields =  ['offer',
                    'title',
                    'time',
                    'optional',
                    'cost'
                    ]
        ordering_fields = ['title']
        nested_depth = 2
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
