import logging
from rest_framework import viewsets
from rest_framework import authentication, permissions
from django.shortcuts import render
from library.viewsets import ModelViewSet
from library.permissions import IsAdminOrAuthenticated, IsAdminOrReadOnly
from django.contrib.sites.models import Site
from django_filters.rest_framework import DjangoFilterBackend
from .filters.category import CategoryFilter
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
from .serializers import (SiteSerializer,
                          EstimateSerializer,
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

_logger = logging.getLogger('midlancer.api.configuration')

class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger

class EstimateViewSet(ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class ProfileTypeViewSet(ModelViewSet):
    queryset = ProfileType.objects.all()
    serializer_class = ProfileTypeSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class BankViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = BaseLanguageSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = BaseLevelSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class ViewStatusViewSet(ModelViewSet):
    queryset = ViewStatus.objects.all()
    serializer_class = ViewStatusSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = BaseSkillSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class ComplainTypeViewSet(ModelViewSet):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class DegreeViewSet(ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrAuthenticated]
    logger = _logger
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter

