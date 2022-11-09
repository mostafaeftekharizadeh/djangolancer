from django.test import TestCase
from rest_framework.test import APIClient
from location.models import Country
from django.contrib.auth.models import User

class ConfigurationTestCase(TestCase):
    fixtures = ['auth.json']

    def setUp(self):
        pass

    def test_country(self):
        data = {
            "name" : "USA",
            "code" : "+98",
            "active" : True
        }
        client = APIClient()
        client.login(username='service', password='ser12345')
        response = client.post('/api/v1/location/country/', data, format='json')
        assert response.status_code == 201
        country = Country.objects.get(name="USA")
        assert country != None

        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        response = client.post('/api/v1/location/country/', data, format='json')
        assert response.status_code == 403

