from .models import Project,Cost,Offer,OfferLevel,Budget
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
