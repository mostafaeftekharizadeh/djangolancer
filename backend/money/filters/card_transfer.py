from django.db.models import Q
from django_filters import FilterSet
from django_filters import rest_framework as filters
from money.models import CardTransfer


class CardTransferFilter(FilterSet):
    owner = filters.CharFilter(method='owner_filter')
    class Meta:
        model = CardTransfer
        fields = ['owner']

    def owner_filter(self, queryset, name, value):
        return queryset
    @property
    def qs(self):
        user = getattr(self.request, 'user', None)
        qs = super().qs
        return  qs.filter(Q(party__user=user))


