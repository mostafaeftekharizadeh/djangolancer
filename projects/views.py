import logging
from rest_framework import viewsets
from rest_framework import authentication, permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from .serializers import (ProjectSerializer,
                          FileSerializer,
                          CostSerializer,
                          OfferSerializer,
                          OfferStepSerializer,
                          BudgetSerializer)
from .models import  Project, File, Cost, Offer, OfferStep, Budget
from .filters.project import ProjectFilter

_logger = logging.getLogger('midlancer.api.projetcs')

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.select_related('party__user')
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter
    logger = _logger

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'head', 'delete']
    logger = _logger

    def get_queryset(self):
        query_set = self.queryset.filter(project=self.kwargs['project'])
        return query_set

class CostViewSet(ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger

class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    #filterset_class = OfferFilter
    logger = _logger

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs['project'])
        query_set = self.queryset.filter(project=project)
        if project.party != self.request.user.party:
            query_set = query_set.filter(party=self.request.user.party)
        return query_set

    def create(self, request, project):
        self.request.data['project'] = project
        return super().create(request, project)

    def update(self, request, project, *args, **kwargs):
        offer = self.get_object()
        if offer.state != 'n':
            raise serializers.ValidationError('Permission Denied!')
        return super().update(request, project)

    @action(detail=True, methods=['get'])
    def accept(self, request, project, args, kwargs,  pk=None):
        offer = self.get_object()
        if offer.project.party != request.user.party:
            raise serializers.ValidationError('Permission Denied!')
        offer.state = 'a'
        offer.save()
        serializer = self.serializer_class(instance=offer,
                                           context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def payment(self, request, project,  pk=None):
        offer = self.get_object()
        if offer.project.party != request.user.party:
            raise serializers.ValidationError('Permission Denied!')
        wallet = offer.project.party.wallet_set.all().first()
        print(wallet.balance)
        print(offer.cost)
        target = offer.party.wallet_set.all().first()
        if wallet.transfer(target, offer.cost) == False:
            raise serializers.ValidationError('Payment Error!')
        offer.state = 'p'
        offer.save()
        serializer = self.serializer_class(instance=offer,
                                           context={'request': request})
        return Response(serializer.data)


class OfferStepViewSet(ModelViewSet):
    queryset = OfferStep.objects.prefetch_related('offerstep_set')
    serializer_class = OfferStepSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger

class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger

class NewViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger
