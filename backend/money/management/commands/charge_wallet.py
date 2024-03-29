"""
wallet charge commands
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    """
    Charging wallet
    """

    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("mobile", nargs="+", type=str)
        parser.add_argument("amount", nargs="+", type=int)

    def handle(self, **options):
        """
        Charging wallet handle
        """
        if options["mobile"][0] == "0":
            users = User.objects.all()
        else:
            users = User.objects.filter(mobile=options["mobile"][0])
        for user in users:
            try:
                wallet = user.party.wallet.all().first()  # type:ignore
            except:
                print(f"user dosent have any wallet{user.mobile}")  # type:ignore
                continue
            wallet.deposit(options["amount"][0])
            print(f"User {user.mobile} charged".format())  # type:ignore
        # except:
        #     pass
