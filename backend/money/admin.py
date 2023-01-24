"""
Money admin
"""
from django.contrib import admin
from .models import Wallet, Transaction, CardTransfer

admin.site.register(Wallet)
admin.site.register(CardTransfer)
admin.site.register(Transaction)
