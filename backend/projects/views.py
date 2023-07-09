"""
Projetcs api endpoints module
"""
import logging
from django.db.models import Q
from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from .serializers import (
    FactorSerializer,
    ProjectSerializer,
    FileSerializer,
    CostSerializer,
    OfferSerializer,
    OfferStepSerializer,
    BudgetSerializer,
    ProjectOfferSerializer,
)
from .models import Project, File, Cost, Offer, OfferStep, Budget
from .filters.project import ProjectFilter

_logger = logging.getLogger("midlancer.api.projetcs")


# pylint: disable=too-many-ancestors
class ProjectViewSet(ModelViewSet):
    """
    Project endpoint Viewset
    """

    queryset = Project.objects.select_related("party__user")
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter
    logger = _logger


class ProjectOfferViewSet(ModelViewSet):
    """
    Project endpoint Viewset
    """

    queryset = Project.objects.select_related("party__user")
    serializer_class = ProjectOfferSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter
    logger = _logger


class FileViewSet(ModelViewSet):
    """
    File endpoint Viewset
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ["get", "post", "head", "delete"]
    logger = _logger

    def get_queryset(self):
        query_set = File.objects.filter(project=self.kwargs["pk"]).all()
        return query_set


class FileListViewSet(ModelViewSet):
    """
    File endpoint Viewset
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ["get"]
    logger = _logger

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs["project"])
        query_set = File.objects.filter(project=project).all()
        return query_set


class CostViewSet(ModelViewSet):
    """
    Cost endpoint Viewset
    """

    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger


class MyOfferViewSet(ModelViewSet):
    """
    my offer endpoint Viewset
    """

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ["get"]
    # filterset_class = OfferFilter
    logger = _logger

    def get_queryset(self):
        """
        get my offer on project
        """
        offer = Offer.objects.all()
        query_set = self.queryset.filter(party=self.request.user.party)

        return query_set


class OfferDeatilViewSet(ModelViewSet):
    """
    return Offer detail endpoint Viewset
    """

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = OfferFilter
    logger = _logger

    def get_queryset(self):
        """
        Offer get function
        """

        query_set = self.queryset.filter(
            Q(pk=self.kwargs["id"]),
            Q(party=self.request.user.party)
            | Q(project__party=self.request.user.party),
        ).all()
        return query_set


class FactorViewSet(ModelViewSet):
    """
    return Offer detail endpoint Viewset
    """

    queryset = Offer.objects.all()
    serializer_class = FactorSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = OfferFilter
    logger = _logger

    def get_queryset(self):
        """
        Offer get function
        """

        query_set = self.queryset.filter(
            Q(pk=self.kwargs["id"]),
            Q(party=self.request.user.party)
            | Q(project__party=self.request.user.party),
        ).all()
        return query_set


class OfferViewSet(ModelViewSet):
    """
    Offer endpoint Viewset
    """

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = OfferFilter
    logger = _logger

    def get_queryset(self):
        """
        Offer get function
        """

        project = Project.objects.get(pk=self.kwargs["project"])
        query_set = self.queryset.filter(project=project)
        if project.party != self.request.user.party:  # type: ignore
            query_set = query_set.filter(party=self.request.user.party)  # type: ignore
        return query_set.order_by("-created_at")

    # override create method
    def create(self, request, project):
        """
        Offer create function
        """

        self.request.data["project"] = project  # type: ignore
        return super().create(request, project)

    def update(self, request, *project, **kwargs):
        """
        Offer update function
        """
        offer = self.get_object()
        if offer.state != "n":
            raise serializers.ValidationError("Permission Denied!")
        return super().update(request, project)

    @action(detail=True, methods=["get"])
    def accept(self, request, project, pk=None):
        """
        Offer accept function
        """
        offer = self.get_object()
        if offer.project.party != request.user.party:
            raise serializers.ValidationError("Permission Denied!")
        offer.state = "a"
        offer.save()
        offer.project.InProgress()
        serializer = self.serializer_class(instance=offer, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def reject(self, request, project, pk=None):
        """
        reject offer by offer id
        """
        offer = self.get_object()
        if offer.project.party != request.user.party:
            raise serializers.ValidationError("Permission Denied!")
        offer.state = "r"
        offer.save()
        serializer = self.serializer_class(instance=offer, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def payment(self, request, project, pk=None):
        """
        Offer payment function
        """
        offer = self.get_object()
        if offer.project.party != request.user.party:
            raise serializers.ValidationError("Permission Denied!")
        wallet = offer.project.party.wallet.all().first()
        target = offer.party.wallet.all().first()
        if not wallet.transfer(target, offer.cost, offer.project):
            if wallet.balance < offer.cost:
                raise serializers.ValidationError("Dont have enough budjet!")
            raise serializers.ValidationError("Payment Error!")
        offer.state = "p"
        offer.save()
        offer.project.Close()
        serializer = self.serializer_class(instance=offer, context={"request": request})
        return Response(serializer.data)


class OfferStepViewSet(ModelViewSet):
    """
    Offer Stepps endpoint Viewset
    """

    queryset = OfferStep.objects.prefetch_related("offerstep_set")
    serializer_class = OfferStepSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger


class BudgetViewSet(ModelViewSet):
    """
    Budget endpoint Viewset
    """

    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger


class NewViewSet(ModelViewSet):
    """
    New endpoint Viewset
    """

    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger
