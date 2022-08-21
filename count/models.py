from django.db import models
from django.contrib.auth.models import User
from configuration.models import Status
# Create your models here.

class Count(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sheba=models.TextField()
    card=models.TextField()
    name=models.TextField()
    bankname = models.TextField()
    active=models.TextField()

class Deposit(models.Model):
    count= models.ForeignKey(Count, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date= models.DateField()
    transaction = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class withdraw(models.Model):
    count= models.ForeignKey(Count, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date= models.DateField()
    transaction = models.TextField()
    to_account= models.IntegerField()
    acc_name= models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class withdraw(models.Model):
    count= models.ForeignKey(Count, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    id_acc =  models.TextField()
    email=  models.TextField()
    name =  models.TextField()
    pos=  models.TextField()
    date= models.DateField()
    amount = models.IntegerField()
    PAY_CHOICES = [
        ("d", 'Deposit'),
        ("w", 'withdraw'),
    ]
    de_wi = models.CharField(
        max_length=1,
        choices=PAY_CHOICES,
        default='m',
        null=True, blank=True
    )
    
    balance = models.IntegerField()