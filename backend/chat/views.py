"""
Chat Api endpoint Viewset
"""
import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
from library.viewsets import ModelViewSet
from .permissions.message import MessagePermission
from .serializers import RoomSerializer, ParticipateSerializer, MessageSerializer
from .models import Room, Participate, Message
from .filters.room import RoomFilter


_logger = logging.getLogger("midlancer.api.chat")


# pylint: disable=too-many-ancestors
class RoomViewSet(ModelViewSet):
    """
    Room endpoint Viewset
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoomFilter
    http_method_names = ["post", "get", "head"]
    logger = _logger


class ParticipateViewSet(ModelViewSet):
    """
    Participate endpoint Viewset
    """

    queryset = Participate.objects.all()
    serializer_class = ParticipateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ["post", "get", "head"]
    logger = _logger


class MessageViewSet(ModelViewSet):
    """
    Message endpoint Viewset
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (MessagePermission,)
    # parser_classes = (MultiPartParser,)
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ["post", "get", "head"]
    logger = _logger

    def get_queryset(self):
        messages = Message.objects.filter(
            room=self.kwargs["room"], party=self.request.user.party
        )
        messages.update(is_seen=True)

        return Message.objects.filter(room=self.kwargs["room"])
