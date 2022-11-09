from rest_framework import viewsets
from rest_framework import authentication, permissions
from django.shortcuts import render
from library.permissions import IsAdminOrReadOnly
from .models import (Estimate,
                     ProfileType,
                     Bank,
                     Language,
                     Level,
                     ViewStatus,
                     Currency,
                     Status,
                     Category,
                     Skill,
                     ComplainType,
                     Degree)
from .serializers import (EstimateSerializer,
                          ProfileTypeSerializer,
                          BankSerializer,
                          BaseLanguageSerializer,
                          BaseLevelSerializer,
                          ViewStatusSerializer,
                          CurrencySerializer,
                          StatusSerializer,
                          CategorySerializer,
                          BaseSkillSerializer,
                          ComplainTypeSerializer,
                          DegreeSerializer)

class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProfileTypeViewSet(viewsets.ModelViewSet):
    queryset = ProfileType.objects.all()
    serializer_class = ProfileTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminOrReadOnly]

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = BaseLanguageSerializer
    permission_classes = [IsAdminOrReadOnly]

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = BaseLevelSerializer
    permission_classes = [IsAdminOrReadOnly]

class ViewStatusViewSet(viewsets.ModelViewSet):
    queryset = ViewStatus.objects.all()
    serializer_class = ViewStatusSerializer
    permission_classes = [IsAdminOrReadOnly]

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAdminOrReadOnly]

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = BaseSkillSerializer
    permission_classes = [IsAdminOrReadOnly]

class ComplainTypeViewSet(viewsets.ModelViewSet):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

