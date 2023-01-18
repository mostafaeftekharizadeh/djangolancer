"""
User Dashboard api endpoints module
"""
import logging
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from .profile_models import Profile
from .dashboard_serializers import DashboardSerializer


_logger = logging.getLogger("midlancer.api.user.dashboard")

# pylint: disable=too-many-ancestors
class DashboardViewSet(ModelViewSet):
    """
    Dashboard api endpoint viewset
    """

    serializer_class = DashboardSerializer
    permission_classes = [IsOwnerOrReadOnly]
    logger = _logger
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = (
            Profile.objects.filter(party_id=self.request.user.party.id)
            .select_related("party__user")
            .prefetch_related("party__party_skill")
            .prefetch_related("party__wallet__transaction")
        )
        return queryset

    def get_object(self):
        self.kwargs["pk"] = self.request.user.party.id
        return super().get_object()
