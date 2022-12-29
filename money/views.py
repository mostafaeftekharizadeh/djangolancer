import logging
from rest_framework import authentication, permissions
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from library.viewsets import ModelViewSet
from .filters.wallet import WalletFilter
from .filters.transaction import TransactionFilter

_logger = logging.getLogger('midlancer.api.count')


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WalletFilter
    logger = _logger
    http_method_names = ['get']


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionFilter
    logger = _logger
    http_method_names = ['get']


