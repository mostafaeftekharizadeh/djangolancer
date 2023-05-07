"""
Complain models
"""
from django.db import models
from configuration.models import Status, ComplainType, ViewStatus
from projects.models import Project
from user.user_models import Party


# Create your models here.
class Complain(models.Model):
    """
    Complain model
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="complain_owner"
    )
    user = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="complain_user"
    )
    date = models.DateField()
    complain_type = models.ForeignKey(ComplainType, on_delete=models.CASCADE)
    price = models.IntegerField()
    viewstatus = models.ForeignKey(ViewStatus, on_delete=models.CASCADE)
    description = models.TextField()
    exp_opinion = models.TextField(null=True)


class ResultComplain(models.Model):
    """
    ResultComplain model
    """

    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    number = models.IntegerField()
    resulte = models.TextField()
    state = models.ForeignKey(Status, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
