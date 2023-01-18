import logging
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser
from .permissions.message import MessagePermission
from .filters.room import RoomFilter
from .serializers import  RoomSerializer, ParticipateSerializer, MessageSerializer
from .models import Room, Participate, Message

_logger = logging.getLogger('midlancer.api.chat')

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoomFilter
    http_method_names = ['post', 'get', 'head']
    logger = _logger

class ParticipateViewSet(ModelViewSet):
    queryset = Participate.objects.all()
    serializer_class = ParticipateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['post', 'get', 'head']
    logger = _logger

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (MessagePermission,)
    parser_classes = (MultiPartParser,)
    http_method_names = ['post', 'get', 'head']
    logger = _logger


