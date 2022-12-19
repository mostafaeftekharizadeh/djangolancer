from django.db.models import Q
from django_filters import FilterSet
from django_filters import rest_framework as filters
from library.filters import CharInFilter
from projects.models import Project


class ProjectFilter(FilterSet):
    owner = filters.CharFilter(method='owner_filter')
    skill = CharInFilter(field_name="skill__name", lookup_expr='in')
    level = CharInFilter(field_name="level__name", lookup_expr='in')
    class Meta:
        model = Project
        fields = ['skill']

    def owner_filter(self, queryset, name, value):
        return queryset
    @property
    def qs(self):
        owner = self.request.query_params.get( 'owner', None)
        user = getattr(self.request, 'user', None)
        parent = super().qs
        if user and user.is_authenticated:
            if owner:
                return parent.filter(Q(party__user=user))
            else:
                return parent.filter(~Q(party__user=user))
        else:
            return parent


