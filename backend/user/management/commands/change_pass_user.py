"""
wallet charge commands
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

# from user.user_models import User


User = get_user_model()


class Command(BaseCommand):
    """
    Add new user
    """

    help = "change user password"

    def add_arguments(self, parser):
        parser.add_argument("mobile", nargs="+", type=str)
        parser.add_argument("newpassword", nargs="+", type=str)

    def handle(self, **options):
        """
        Add new user handle
        """
        u = User.objects.get(mobile=options["mobile"][0])
        u.set_password(options["newpassword"][0])
        u.save()

        print(f"User {u.mobile} password changed !".format())  # type:ignore
