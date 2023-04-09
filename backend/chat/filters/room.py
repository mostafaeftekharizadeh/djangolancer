from django.db.models import Q
from django_filters import FilterSet
from django_filters import rest_framework as filters
from library.filters import CharInFilter
from chat.models import Room



class RoomFilter(FilterSet):
    status = CharInFilter(field_name="project__status")
    #skill = CharInFilter(field_name="party__party_skill__skill__name", lookup_expr='in')
    #firstname = filters.CharFilter(field_name="party__user__first_name", lookup_expr='icontains')
    #lastname = filters.CharFilter(field_name="party__user__last_name", lookup_expr='icontains')
    class Meta:
        model = Room
        fields = ["party", "project", "status"]
    @property
    def qs(self):
        user = getattr(self.request, 'user', None)
        qs = super().qs
        return  qs.filter(Q(chat_participate__party__user=user)).distinct()




