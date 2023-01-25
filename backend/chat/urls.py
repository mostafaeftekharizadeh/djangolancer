"""
Chat urls
"""
from rest_framework import routers
from . import views


urlpatterns = []


router = routers.DefaultRouter()
router.register(r"chat/room", views.RoomViewSet, basename="room")
router.register(r"chat/participate", views.ParticipateViewSet, basename="participate")
router.register(
    r"chat/message/(?P<room>[^/]+)", views.MessageViewSet, basename="message"
)
