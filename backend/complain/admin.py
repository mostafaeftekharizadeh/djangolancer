"""
Complain  admin
"""
from django.contrib import admin
from .models import Complain, ResultComplain


# Register your models here.
admin.site.register(Complain)
admin.site.register(ResultComplain)
