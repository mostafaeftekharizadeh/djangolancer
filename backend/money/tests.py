"""
Money test case
"""
from django.urls import reverse

from rest_framework import status
from django.test import TestCase
from django.contrib import auth
from .models import Party, Wallet

# from rest_framework.test import APITestCase


class MoneyViewSetTests(TestCase):
    fixtures = ["user.json", "level.json", "category.json", "skill.json"]

    def test_getmoney(self):
        self.client.login(username="989120000014", password="1")
        user = auth.get_user(self.client)
        assert user.is_authenticated
        response = self.client.get("/api/v1/money/transaction/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_postmoney(self):
        self.client.login(username="989120000010", password="1")
        user = auth.get_user(self.client)
        party = Party.objects.first()
        walet = Wallet.objects.create(party=party)
        data = {
            "party": party,
            "number": 1,
            "shaba": "123456789123456789123",
            "value": 100000,
        }
        assert user.is_authenticated
        response = self.client.post("/api/v1/money/transfer/", data=data, format="json")
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
