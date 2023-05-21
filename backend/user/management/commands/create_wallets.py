"""
wallet create commands
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from money.models import Wallet

User = get_user_model()


class Command(BaseCommand):
    """
    wallet create
    """

    help = "create user wallet if not exists"

    def handle(self, **options):
        """
        wallet create handel
        """
        users = User.objects.all()
        for user in users:
            try:
                if len(user.party.wallet.all()) == 0:  # type:ignore
                    try:
                        Wallet.objects.create(party=user.party)  # type:ignore
                        print(f"wallet {user.mobile} created!".format())  # type:ignore
                    except:
                        print(
                            f"user dosent have any wallet:{user.mobile} !".format()
                        )  # type:ignore
                        continue
                print(f"wallet {user.mobile} created!".format())  # type:ignore
            except:
                pass
