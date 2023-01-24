"""
Money App config
"""
from django.apps import AppConfig


class MoneyConfig(AppConfig):
    """
    Money config
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "money"
