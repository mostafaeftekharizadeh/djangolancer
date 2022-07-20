from django.contrib import admin
from .models import Estimate
# Register your models here.

class EstimateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Estimate, EstimateAdmin)
