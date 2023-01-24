"""
User Admin panel register
"""
from django.contrib import admin
from user.profile_models import (
    Profile,
    Contact,
    Skill,
    Job,
    Education,
    Certificate,
    Specialty,
    Achievement,
    Language,
    WorkSample,
    Experience,
    SocialMedia,
    Vote,
)
from user.user_models import User, Party, Otp

# Register your models here.

admin.site.register(User)
admin.site.register(Party)
admin.site.register(Otp)

admin.site.register(Education)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Specialty)
admin.site.register(Achievement)
admin.site.register(Language)
admin.site.register(WorkSample)
admin.site.register(Experience)
admin.site.register(SocialMedia)
admin.site.register(Vote)
