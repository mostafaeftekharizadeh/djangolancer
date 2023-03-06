"""
Projetc filter module
"""
from django.db.models import Q
from django_filters import FilterSet
from django_filters import rest_framework as filters
from projects.models import Project
from library.filters import CharInFilter
from configuration.models import Skill


class ProjectFilter(FilterSet):
    """
    Projetc filter class
    """

    owner = filters.CharFilter(method="owner_filter")
    q = filters.CharFilter(method="owner_filter")
    skill = CharInFilter(field_name="skill__name", lookup_expr="in")
    level = CharInFilter(field_name="level__name", lookup_expr="in")

    class Meta:
        model = Project
        fields = ["skill"]

    def owner_filter(self, queryset, name, value):
        """
        Projetc filter owner
        """
        return queryset

    @property
    def qs(self):
        owner = self.request.query_params.get("owner", None)
        q = self.request.query_params.get("q", None)
        user = getattr(self.request, "user", None)
        qs = super().qs
        if user and user.is_authenticated:
            if owner:
                qs = qs.filter(Q(party__user=user))
            else:
                qs = qs.filter(~Q(party__user=user))

        if q:
            #qs = qs.distinct()
            skills = Skill.objects.filter(name__icontains=q)
            print(skills)
            qs = qs.filter(
                #Q(skill__name__icontains=q)
                Q(skill__in=skills)
                #| Q(level__name=q)
                | Q(category__name=q)
                #| Q(sub_category__name=q)
                #| Q(title__icontains=q)
            )
        print(qs.query)
        return qs
