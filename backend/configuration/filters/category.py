from django_filters import FilterSet
from django_filters import rest_framework as filters
from configuration.models import Category


class CategoryFilter(FilterSet):
    """
    Filter base class for category filtring
    """

    parent = filters.CharFilter(field_name="parent")
    root = filters.BooleanFilter(
        field_name="parent",
        lookup_expr="isnull",
        help_text="set it to 1 if you want to get root objects",
    )
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ["parent", "name", "root"]
