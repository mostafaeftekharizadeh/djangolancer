"""
Configuration api endpoints module
"""
import logging

from django.contrib.sites.models import Site
from django_filters.rest_framework import DjangoFilterBackend
from library.viewsets import ModelViewSet
from library.permissions import IsAdminOrReadOnly
from .filters.category import CategoryFilter
from .models import (
    Estimate,
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
    Degree,
)
from .serializers import (
    SiteSerializer,
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
    DegreeSerializer,
)
from django.db.models import Q, Count

# pylint: disable=too-many-ancestors
_logger = logging.getLogger("midlancer.api.configuration")


class SiteViewSet(ModelViewSet):
    """
    Site endpoint Viewset
    """

    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class EstimateViewSet(ModelViewSet):
    """
    Estimate endpoint Viewset
    """

    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class ProfileTypeViewSet(ModelViewSet):
    """
    Profile Type endpoint Viewset
    """

    queryset = ProfileType.objects.all()
    serializer_class = ProfileTypeSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class BankViewSet(ModelViewSet):
    """
    Banks Name endpoint Viewset
    """

    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class LanguageViewSet(ModelViewSet):
    """
    Language endpoint Viewset
    """

    queryset = Language.objects.all()
    serializer_class = BaseLanguageSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class LevelViewSet(ModelViewSet):
    """
    Level endpoint Viewset
    """

    queryset = Level.objects.all()
    serializer_class = BaseLevelSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class ViewStatusViewSet(ModelViewSet):
    """
    View Status endpoint Viewset
    """

    queryset = ViewStatus.objects.all()
    serializer_class = ViewStatusSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class CurrencyViewSet(ModelViewSet):
    """
    Currency endpoint Viewset
    """

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class StatusViewSet(ModelViewSet):
    """
    Status endpoint Viewset
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class SkillViewSet(ModelViewSet):
    """
    Skill endpoint Viewset
    """

    queryset = Skill.objects.all()
    serializer_class = BaseSkillSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class ComplainTypeViewSet(ModelViewSet):
    """
    Complain endpoint Viewset
    """

    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class DegreeViewSet(ModelViewSet):
    """
    Degree endpoint Viewset
    """

    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger


class CategoryViewSet(ModelViewSet):
    """
    Category endpoint Viewset
    """

    queryset = Category.objects.filter(active=True).annotate(
        num_projects=Count("project_category", filter=Q(project_category__status="n")),
        num_subcat=Count("project_sub_category"),
    )
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    logger = _logger
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter


class AllCategoryViewSet(ModelViewSet):
    """
    Category endpoint Viewset
    """

    pagination_class = None

    queryset = (
        Category.objects.filter(active=True)
        .annotate(
            num_projects=Count(
                "project_category", filter=Q(project_category__status="n")
            ),
            num_subcat=Count("project_sub_category"),
        )
        .all()
    )
    serializer_class = CategorySerializer
    logger = _logger
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
