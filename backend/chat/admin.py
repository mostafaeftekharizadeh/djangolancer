"""
Chat admin module
"""
from django.contrib import admin
from chat.models import Room, Participate, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Participate)
admin.site.register(Message)
