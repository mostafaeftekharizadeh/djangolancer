import os
import hashlib
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from library.models import BaseModel
from user.user_models import Party
from projects.models import Project



class Room(BaseModel):
    party = models.ForeignKey(Party, null=False, related_name="chat_room", on_delete=models.CASCADE)
    user = models.ForeignKey(Party, null=False, related_name="chat_user", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)

class Participate(BaseModel):
    party = models.ForeignKey(Party, null=False, related_name="chat_participate", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=False, related_name="chat_participate", on_delete=models.CASCADE)
    archived = models.BooleanField(default=False, null=True,blank=True)

class Message(BaseModel):
    def hash_upload(instance, filename):
        fname, ext = os.path.splitext(filename)
        return "message/{0}{1}".format(instance.id, ext)
    party = models.ForeignKey(Party, null=False, related_name="source", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=False, related_name="target", on_delete=models.CASCADE)
    media = models.ImageField(upload_to=hash_upload, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=True,blank=True)

