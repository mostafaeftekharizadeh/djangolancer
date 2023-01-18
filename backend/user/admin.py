"""
User Admin panel register
"""
from django.contrib import admin
from user.profile_models import Profile, Education
from user.user_models import User

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    """
    User module Profile Admin
    """

    pass


admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education)
