from django.test import TestCase
from rest_framework.test import APIClient
from location.models import Country,State,City,Place
from django.contrib.auth.models import User

class ConfigurationTestCase(TestCase):
    fixtures = ['auth.json']

    def setUp(self):
        pass

    def test_country(self):
        data = {
            "name" : "Iran",
            "initials": "IR",
            "code" : "+98",
            "active" : True
        }
        client = APIClient()
        client.login(username='service', password='ser12345')
        response = client.post('/api/v1/location/country/', data, format='json')
        assert response.status_code == 201
        country = Country.objects.get(name="Iran")
        assert country != None

        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        response = client.post('/api/v1/location/country/', data, format='json')
        assert response.status_code == 403

    def test_state(self):
        country_pk = Country.objects.get(name="Iran")
        
        data = {
            "name" : "Tehran",
            "code" : "021",
            "country":country_pk,
            "initials": "TEH",            
            "active" : True
        }
        client = APIClient()
        client.login(username='service', password='ser12345')
        response = client.post('/api/v1/location/state/', data, format='json')
        assert response.status_code == 201
        state = State.objects.get(name="Tehran")
        assert state != None

        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        response = client.post('/api/v1/location/state/', data, format='json')
        assert response.status_code == 403

    def test_city(self):
        state_pk = State.objects.get(name="Tehran")
             
        data = {
            "name" : "Tehran",
            "state": state_pk,         
            "active" : True
        }
        client = APIClient()
        client.login(username='service', password='ser12345')
        response = client.post('/api/v1/location/city/', data, format='json')
        assert response.status_code == 201
        city = City.objects.get(name="Tehran")
        assert city != None

        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        response = client.post('/api/v1/location/city/', data, format='json')
        assert response.status_code == 403

    def test_place(self):
        data = {
            "name" : "InOffice",            
            "active" : True
        }
        client = APIClient()
        client.login(username='service', password='ser12345')
        response = client.post('/api/v1/location/place/', data, format='json')
        assert response.status_code == 201
        place = Place.objects.get(name="InOffice")
        assert place != None

        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        response = client.post('/api/v1/location/place/', data, format='json')
        assert response.status_code == 403