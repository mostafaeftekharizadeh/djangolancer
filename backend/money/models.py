"""
Money models
"""
from django.db import models
from library.models import BaseModel
from user.user_models import Party
from projects.models import Project
from configuration.models import Bank


class Wallet(BaseModel):
    """
    Money wallet model
    """

    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="wallet")
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def deposit(self, value, target=None, project=None, card=None):
        """
        Money wallet deposite action
        """
        self.transaction.create(  # type:ignore
            value=value,
            target=target,
            project=project,
            card=card,
            balance=self.balance + value,
        )
        self.balance += value
        self.save()
        return True

    def withdraw(self, value, target=None, project=None, card=None):
        """
        Money wallet withdraw action
        """
        print("self.balance - value")
        print(self.balance - value)
        if value > self.balance or self.balance - value < 0:
            return False

        transaction = self.transaction.create(  # type:ignore
            value=-value,
            target=target,
            project=project,
            card=card,
            balance=self.balance - value,
        )
        print(value)
        self.balance -= value
        self.save()
        return transaction

    def transfer(self, wallet, value, project=None):
        """
        Money wallet transfer action
        """
        transaction = self.withdraw(value, wallet, project)
        if transaction:
            wallet.deposit(value, self, project)
            return transaction

        return False

    def __str__(self):
        return (
            self.party.user.first_name
            + " "
            + self.party.user.last_name
            + "-"
            + self.party.user.mobile
            + "::"
            + str(self.balance)
        )


class CardTransfer(BaseModel):
    """
    Money card model
    """

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    number = models.BigIntegerField(default=0)
    shaba = models.CharField(default="", max_length=24)
    value = models.BigIntegerField(default=0)
    STATE_CHOICES = [
        ("i", "In Progress"),
        ("p", "Completed"),
    ]
    state = models.CharField(
        max_length=1, choices=STATE_CHOICES, default="i", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    transfered_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        wallet = Wallet.objects.get(party=self.party)
        transaction = wallet.withdraw(self.value)
        if transaction:
            super().save(args, kwargs)
            transaction.card = self
            transaction.save()
            return True
        return False


class Transaction(BaseModel):
    """
    Money Transaction model
    """

    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="transaction"
    )
    target = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="target", null=True, blank=True
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    card = models.ForeignKey(CardTransfer, on_delete=models.CASCADE, null=True)
    value = models.BigIntegerField(default=0)
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #    return "{} : amount {}".format(self.wallet.user.first_name, self.value)
