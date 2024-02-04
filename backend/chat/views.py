"""
Chat Api endpoint Viewset
"""
import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
from library.permissions import IsOwnerOrReadOnly
from library.viewsets import ModelViewSet
from .permissions.message import MessagePermission
from .serializers import RoomSerializer, ParticipateSerializer, MessageSerializer
from .models import Room, Participate, Message
from .filters.room import RoomFilter
from rest_framework.views import APIView
from rest_framework.response import Response

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
        messages = Message.objects.filter(room=self.kwargs["room"]).exclude(
            party=self.request.user.party
        )
        messages.update(is_seen=True)
        return Message.objects.filter(room=self.kwargs["room"])


class AllMessageViewSet(ModelViewSet):
    """
    Message endpoint Viewset
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = (MessagePermission,)
    # parser_classes = (MultiPartParser,)
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ["get"]
    logger = _logger

    def get_queryset(self):
        messages = Message.objects.all()
        messages.update(is_seen=True)
        return Message.objects.all()


class FilesList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = OfferFilter
    logger = _logger

    def get(self, request, projectid):
        messages = Message.objects.filter(
            room__project=self.kwargs["projectid"], party=self.request.user.party
        ).exclude(media="")
        other = (
            Message.objects.filter(room__project=self.kwargs["projectid"])
            .exclude(media="")
            .exclude(party=self.request.user.party)
        )

        data = {
            "my_files": MessageSerializer(messages, many=True).data,
            "other_files": MessageSerializer(other, many=True).data,
        }
        return Response(data)

    # def get(self, request, project):
    #     """
    #     Offer get function
    #     """

    #     messages = (
    #         Message.objects.filter(room=self.kwargs["room"])
    #         .exclude(media__isnull=True)
    #         .all()
    #     )
    #     query_set = Offer.objects.filter(project=project).all()
    #     if project.party != request.user.party:  # type: ignore
    #         query_set = query_set.filter(party=request.user.party).all()  # type: ignore
    #     data = {"messages": MessageSerializer(messages)}
    #     return Response(data)
