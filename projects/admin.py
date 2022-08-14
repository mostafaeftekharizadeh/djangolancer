from django.contrib import admin
from projects.models import Project,File,Cost,Offer,OfferLevel,Budget



class ProjectAdmin(admin.ModelAdmin):
    pass
class FileAdmin(admin.ModelAdmin):
    pass
class CostAdmin(admin.ModelAdmin):
    pass
class OfferAdmin(admin.ModelAdmin):
    pass
class OfferLevelAdmin(admin.ModelAdmin):
    pass
class BudgetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferLevel, OfferLevelAdmin)
admin.site.register(Budget, BudgetAdmin)