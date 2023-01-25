"""
Complain views Api 
"""
import logging
from rest_framework import permissions
from library.viewsets import ModelViewSet
from .models import Complain, ResultComplain
from .serializers import ComplainSerializer, ResultComplainSerializer


_logger = logging.getLogger("midlancer.api.complain")


class ComplainViewSet(ModelViewSet):
    """
    Complain endpoint Viewset
    """

    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post", "get", "head"]
    logger = _logger


class ResultComplainViewSet(ModelViewSet):
    """
    ResultComplain endpoint Viewset
    """

    queryset = ResultComplain.objects.all()
    serializer_class = ResultComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post", "get", "head"]
    logger = _logger
