from datetime import datetime
from email.policy import default
from django.db import models
from library.models import BaseModel
from configuration.models import Status, Bank
from user.user_models import Party
from projects.models import Project


class Wallet(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='wallet')
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def deposit(self, value, target=None, project=None, card=None):
        self.transaction_set.create(
            value=value,
            target=target,
            project=project,
            card=card,
            balance=self.balance + value
        )
        self.balance += value
        self.save()
        return True

    def withdraw(self, value, target=None, project=None, card=None):

        if value > self.balance:
            return False

        transaction = self.transaction_set.create(
            value=-value,
            target=target,
            project=project,
            card=card,
            balance=self.balance - value
        )
        self.balance -= value
        self.save()
        return transaction

    def transfer(self, wallet, value, project=None):
        transaction = self.withdraw(value, wallet, project)
        if transaction:
            wallet.deposit(value, self, project)
            return transaction
        else:
            return False

class CardTransfer(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    number = models.BigIntegerField(default=0)
    shaba = models.CharField(default="", max_length=24)
    value = models.BigIntegerField(default=0)
    STATE_CHOICES = [
        ("i", 'In Progress'),
        ("p", 'Completed'),
    ]
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default='i',
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    transfered_at = models.DateTimeField(null=True, blank=True)
    def save(self, *args, **kwargs):
        wallet = Wallet.objects.get(party=self.party)
        transaction = wallet.withdraw(self.value)
        if transaction:
            instance = super().save(*args, **kwargs)
            transaction.card = self
            transaction.save()
            return instance
        else:
            return False

class Transaction(BaseModel):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transaction')
    target = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='target', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    card = models.ForeignKey(CardTransfer, on_delete=models.CASCADE, null=True)
    value = models.BigIntegerField(default=0)
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    #def __str__(self):
    #    return "{} : amount {}".format(self.wallet.user.first_name, self.value)


