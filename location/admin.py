from django.contrib import admin
from location.models import Country, State, City, Place

class CountryAdmin(admin.ModelAdmin):
    pass
class StateAdmin(admin.ModelAdmin):
    pass
class CityAdmin(admin.ModelAdmin):
    pass
class PlaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)

