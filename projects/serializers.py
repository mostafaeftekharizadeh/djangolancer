from .models import Project,File,Cost,Offer,OfferLevel,Budget
from rest_framework import serializers




class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =  ['profile',
                    'category',
                    'work',
                    'title', 
                    # 'file_upload_img',
                    'skills',
                    'exp_time',
                    'description',
                    # 'file_upload_des',
                    'currency',
                    'budget_min',
                    'budget_max',
                    'tag',
                    'cre_price', 
                    'budget_total', 
                    'expire_date',
                    'discount' ,
                    'date' ,
                    'status', 
                    'level' ,
                    'place' ,
                    'country', 
                    'state' ,
                    'city' ,
                    ]
        ordering_fields = ['title']
        nested_depth = 2
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields =  ['project'
                    ]
        # ordering_fields = ['title']
        # nested_depth = 2
class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields =  ['Project',
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
                    'profile',
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