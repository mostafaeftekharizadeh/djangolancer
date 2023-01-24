"""
Location Admin model
"""
from django.contrib import admin
from location.models import Country, State, City, Place


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Place)
