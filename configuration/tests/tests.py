from django.test import TestCase
from rest_framework.test import APIClient
from configuration.models import Bank
from django.contrib.auth.models import User

class ConfigurationTestCase(TestCase):
    fixtures = ['auth.json']

    def setUp(self):
        pass

    def test_bank(self):
        data = {
            "name" : "test bank",
            "active" : True
        }
        client = APIClient()
        client.login(username='service', password='ser12345')
        response = client.post('/api/v1/configuration/bank/', data, format='json')
        assert response.status_code == 201
        bank = Bank.objects.get(name="test bank")
        assert bank != None

        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        response = client.post('/api/v1/configuration/bank/', data, format='json')
        assert response.status_code == 403

