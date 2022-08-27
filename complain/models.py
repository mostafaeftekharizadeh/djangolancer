from django.db import models
from django.contrib.auth.models import User
from user.models import Profile
from configuration.models import Skill,Status,Level
from configuration.models import ComplainType,ViewStatus,Status
from projects.models import Project
# Create your models here.
class Complain(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner= models.ForeignKey(User, on_delete=models.CASCADE,related_name="complain_owner")
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="complain_user")
    date = models.DateField()
    complain_type=models.ForeignKey(ComplainType, on_delete=models.CASCADE)
    price =models.IntegerField()
    viewstatus=models.ForeignKey(ViewStatus, on_delete=models.CASCADE)
    description=models.TextField()
    exp_opinion=models.TextField(null=True)


class ResultComplain(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    number=models.IntegerField()
    resulte=models.TextField()
    state=models.ForeignKey(Status, on_delete=models.CASCADE)
    date = models.DateField()
    description=models.TextField()
