from django.contrib import admin
from .models import *
# Register your models here.

class EstimateAdmin(admin.ModelAdmin):
    pass
class ProfileTypeAdmin(admin.ModelAdmin):
    pass
class BankAdmin(admin.ModelAdmin):
    pass
class LanguageAdmin(admin.ModelAdmin):
    pass
class LevelAdmin(admin.ModelAdmin):
    pass
class ViewStatusAdmin(admin.ModelAdmin):
    pass
class CurrencyAdmin(admin.ModelAdmin):
    pass
class StatusAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass
class SkillAdmin(admin.ModelAdmin):
    pass
class ComplainTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Estimate, EstimateAdmin)
admin.site.register(ProfileType, ProfileTypeAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(ViewStatus, ViewStatusAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(ComplainType, ComplainTypeAdmin)



