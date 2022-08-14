from rest_framework import viewsets
from rest_framework import authentication, permissions
from django.shortcuts import render
from .models import Skill,WorkCategory,Level,Estimate
from .serializers import SkillSerializer,WorkCategorySerializer,LevelSerializer,EstimateSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class WorkCategoryViewSet(viewsets.ModelViewSet):
    queryset = WorkCategory.objects.all()
    serializer_class = WorkCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ('GET',)
