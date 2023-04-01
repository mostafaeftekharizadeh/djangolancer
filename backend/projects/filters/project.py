"""
Projetc filter module
"""
from django.db.models import Q
from django_filters import FilterSet
from django_filters import rest_framework as filters
from projects.models import Project
from library.filters import CharInFilter
from configuration.models import Skill, Level, Category


class ProjectFilter(FilterSet):
    """
    Projetc filter class
    """

    owner = filters.CharFilter(method="owner_filter")
    q = filters.CharFilter(method="owner_filter")
    skill = CharInFilter(field_name="skill", lookup_expr="in")
    level = CharInFilter(field_name="level", lookup_expr="in")
    category = CharInFilter(field_name="category", lookup_expr="in")
    sub_category = CharInFilter(field_name="sub_category", lookup_expr="in")

    class Meta:
        model = Project
        fields = ["skill", "level", "category", "sub_category", "q", "owner"]

    def owner_filter(self, queryset, name, value):
        """
        Projetc filter owner
        """
        if self.request.user and self.request.user.is_authenticated:
            return queryset.filter(party__user=self.request.user)
        return queryset

    @property
    def qs(self):
        q = self.request.query_params.get("q", None)
        user = getattr(self.request, "user", None)
        qs = super().qs
        #owner = self.request.query_params.get("owner", None)
        #if user and user.is_authenticated:
        #    if owner:
        #        qs = qs.filter(Q(party__user=user))
        #    else:
        #        qs = qs.filter(~Q(party__user=user))

        if q:
            qs = qs.filter(
                Q(title__icontains=q)
            )
        print(qs.query)
        return qs
