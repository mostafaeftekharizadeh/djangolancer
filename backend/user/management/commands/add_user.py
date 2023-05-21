"""
wallet charge commands
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from user.user_models import Party
from user.profile_models import Profile
from money.models import Wallet

User = get_user_model()


class Command(BaseCommand):
    """
    Add new user
    """

    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("mobile", nargs="+", type=str)
        parser.add_argument("password", nargs="+", type=str)
        parser.add_argument("firstname", nargs="+", type=str)
        parser.add_argument("lastname", nargs="+", type=str)
        #parser.add_argument("email", nargs="+", type=str)

    def handle(self, **options):
        """
        Add new user handle
        """
        user = User()
        user.mobile = options['mobile'][0]
        user.username = options['mobile'][0]
        user.firstname = options['firstname'][0]
        user.lastname = options['lastname'][0]
        user.set_password(options['password'][0])
        user.save()
        party = Party.objects.create(user=user)
        Profile.objects.create(party=party)
        Wallet.objects.create(party=party)
        print(f"User {user.mobile} added!".format())  # type:ignore
