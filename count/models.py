from datetime import datetime
from email.policy import default
from django.db import models
from library.models import BaseModel
from configuration.models import Status, Bank
from user.user_models import Party
# Create your models here.


class Count(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    sheba = models.CharField(max_length=26, unique=True)
    card = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=255)
    bankname = models.ForeignKey(Bank, on_delete=models.CASCADE)
    active = models.TextField()

class Deposit(BaseModel):
    count = models.ForeignKey(Count, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
    transaction = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

class Withdraw(BaseModel):
    count = models.ForeignKey(Count, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
    transaction = models.IntegerField()
    to_account = models.IntegerField()
    acc_name = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

class Account(BaseModel):
    count = models.ForeignKey(Count, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    pos = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now)
    amount = models.IntegerField()
    PAY_CHOICES = [
        ("d", 'Deposit'),
        ("w", 'withdraw'),
    ]
    de_wi = models.CharField(
        max_length=1,
        choices=PAY_CHOICES,
        default='d',
        null=True, blank=True
    )
    balance = models.IntegerField()
