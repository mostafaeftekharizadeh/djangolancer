from django.db import models
from user.models import Party

class Company(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE,null=False, blank=False)
    name = models.CharField(max_length=255)

