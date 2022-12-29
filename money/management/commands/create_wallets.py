from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from money.models import Wallet

User = get_user_model()

class Command(BaseCommand):
    help = 'create user wallet if not exists'
    def handle(self, **options):
        user = User.objects.all()
        try:
            if len(user.party.wallet_set.all()) == 0:
                wallet = Wallet.objects.create(party = user.party)
        except:
            pass
        print("Wallets created!")
