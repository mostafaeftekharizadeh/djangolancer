"""
Project admin
"""
from django.contrib import admin
from projects.models import Project, File, Cost, Offer, OfferStep, Budget


admin.site.register(Project)
admin.site.register(File)
admin.site.register(Cost)
admin.site.register(Offer)
admin.site.register(OfferStep)
admin.site.register(Budget)
