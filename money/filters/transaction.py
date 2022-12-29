from django.db.models import Q
from django_filters import FilterSet
from django_filters import rest_framework as filters
from money.models import Transaction


class TransactionFilter(FilterSet):
    owner = filters.CharFilter(method='owner_filter')
    class Meta:
        model = Transaction
        fields = ['owner']

    def owner_filter(self, queryset, name, value):
        return queryset
    @property
    def qs(self):
        user = getattr(self.request, 'user', None)
        qs = super().qs
        return  qs.filter(Q(wallet__party__user=user))


