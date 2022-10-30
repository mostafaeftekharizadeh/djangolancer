from django.contrib import admin
from user.models import Profile, Education

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education)
