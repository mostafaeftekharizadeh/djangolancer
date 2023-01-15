import logging
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .filters.profile import ProfileFilter
from rest_framework import permissions
from library.viewsets import ModelViewSet
from library.permissions import IsOwnerOrReadOnly
from .profile_models import Profile, Skill

from .dashboard_serializers import DashboardSerializer


_logger = logging.getLogger("midlancer.api.user.dashboard")

class DashboardViewSet(ModelViewSet):
    serializer_class = DashboardSerializer
    permission_classes = [IsOwnerOrReadOnly]
    logger = _logger
    http_method_names = ['get']
    def get_queryset(self):
        queryset = Profile.objects.filter(party_id=self.request.user.party.id)\
                    .select_related('party__user')\
                    .prefetch_related('party__party_skill')\
                    .prefetch_related('party__wallet__transaction')
        return queryset
    def get_object(self):
        self.kwargs['pk']  = self.request.user.party.id
        return super(DashboardViewSet, self).get_object()


