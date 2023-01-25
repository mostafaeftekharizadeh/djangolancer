"""
Configuration  admin
"""
from django.contrib import admin
from .models import (
    Estimate,
    ProfileType,
    Bank,
    Language,
    Level,
    ViewStatus,
    Currency,
    Status,
    Category,
    Skill,
    ComplainType,
    Degree,
)

# Register your models here.
admin.site.register(Estimate)
admin.site.register(ProfileType)
admin.site.register(Bank)
admin.site.register(Language)
admin.site.register(Level)
admin.site.register(ViewStatus)
admin.site.register(Currency)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(ComplainType)
admin.site.register(Degree)
