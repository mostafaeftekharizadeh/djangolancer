"""
Profile filter
"""
from django_filters import FilterSet
from django_filters import rest_framework as filters
from library.filters import CharInFilter
from user.profile_models import Profile


class ProfileFilter(FilterSet):
    skill = CharInFilter(field_name="party__party_skill__skill__name", lookup_expr="in")
    firstname = filters.CharFilter(
        field_name="party__user__first_name", lookup_expr="icontains"
    )
    lastname = filters.CharFilter(
        field_name="party__user__last_name", lookup_expr="icontains"
    )

    class Meta:
        model = Profile
        fields = ["party", "gender"]
