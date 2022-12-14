import logging
from rest_framework import viewsets
from rest_framework import authentication, permissions
from rest_framework.parsers import FormParser, MultiPartParser
from location.serializers import PlaceSerializer, CountrySerializer, StateSerializer, CitySerializer, PlaceSerializer
from location.models import Country, State, City, Place
from rest_framework import generics
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from .serializers import ProjectSerializer, FileSerializer, CostSerializer, OfferSerializer, OfferLevelSerializer, BudgetSerializer
from .models import  Project, File, Cost, Offer, OfferLevel, Budget
from django_filters.rest_framework import DjangoFilterBackend
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly

_logger = logging.getLogger('midlancer.api.projetcs')

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.select_related('party__user')\
                                    .prefetch_related('skill')
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends =  [DjangoFilterBackend]
    filterset_fields = ('country', 'state', 'city',
                        'skill', 'party', 'level', 'place','category')
    logger = _logger

    '''
    filter projects based on owner
    '''
    def get_queryset(self):
        if self.request.GET.get('owner') == '1':
            return Project.objects.filter(party__user=self.request.user)
        else:
            return Project.objects.all().exclude(party__user=self.request.user)


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['post', 'head', 'delete']
    logger = _logger


class CostViewSet(ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    logger = _logger


class OfferLevelViewSet(ModelViewSet):
    queryset = OfferLevel.objects.all()
    serializer_class = OfferLevelSerializer
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
