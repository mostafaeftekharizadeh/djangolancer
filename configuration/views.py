from rest_framework import viewsets
from rest_framework import authentication, permissions
from django.shortcuts import render
from .models import Estimate,ProfileType,BankName,Language,Level,ViewStatus,Currency,Status,Category,Skill,ComplainType,Degree
from .serializers import EstimateSerializer,ProfileTypeSerializer,BankNameSerializer,LanguageSerializer,LevelSerializer,ViewStatusSerializer,CurrencySerializer,StatusSerializer,CategorySerializer,SkillSerializer,ComplainTypeSerializer,DegreeSerializer

class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class ProfileTypeViewSet(viewsets.ModelViewSet):
    queryset = ProfileType.objects.all()
    serializer_class = ProfileTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class BankNameViewSet(viewsets.ModelViewSet):
    queryset = BankName.objects.all()
    serializer_class = BankNameSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class ViewStatusViewSet(viewsets.ModelViewSet):
    queryset = ViewStatus.objects.all()
    serializer_class = ViewStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class ComplainTypeViewSet(viewsets.ModelViewSet):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',) 
class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)


class CategoryViewSet(viewsets.ModelViewSet):                                                              
     queryset = Category.objects.all()                                                                      
     serializer_class = CategorySerializer                                   
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]                                               
     allowed_methods = ('GET',)