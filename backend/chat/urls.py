"""
Chat urls
"""
from django.urls import path
from rest_framework import routers
from . import views


urlpatterns = [
    path(r"api/v1/chat/filelist/<str:projectid>/", views.FilesList.as_view())
]


router = routers.DefaultRouter()
router.register(r"chat/room", views.RoomViewSet, basename="room")
router.register(r"chat/participate", views.ParticipateViewSet, basename="participate")
router.register(
    r"chat/message/(?P<room>[^/]+)", views.MessageViewSet, basename="message"
)
router.register(r"chat/allmessage", views.AllMessageViewSet, basename="allmessage")
# router.register(r"chat/filelist/(?P<room>[^/]+)", views.FilesList, basename="filelist")
