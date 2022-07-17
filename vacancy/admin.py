from django.contrib import admin
from vacancy.models import Vacancy, Skill, Category, Level

class VacancyAdmin(admin.ModelAdmin):
    pass
class SkillAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass
class LevelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Level, LevelAdmin)

