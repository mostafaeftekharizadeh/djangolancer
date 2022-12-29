from datetime import datetime
from email.policy import default
from django.db import models
from library.models import BaseModel
from configuration.models import Status, Bank
from user.user_models import Party

class Wallet(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def deposit(self, value, target=None):
        self.transaction_set.create(
            value=value,
            target=target,
            balance=self.balance + value
        )
        self.balance += value
        self.save()
        return True

    def withdraw(self, value, target=None):

        if value > self.balance:
            return False

        self.transaction_set.create(
            value=-value,
            target=target,
            balance=self.balance - value
        )
        self.balance -= value
        self.save()
        return True

    def transfer(self, wallet, value):
        if self.withdraw(value, wallet):
            wallet.deposit(value, self)
            return True
        else:
            return False

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    target = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='target', null=True, blank=True)
    value = models.BigIntegerField(default=0)
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} : amount {}".format(self.wallet.user.first_name, self.value)



