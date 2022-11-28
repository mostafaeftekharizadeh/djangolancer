from django.test import TestCase
from rest_framework.test import APIClient
from location.models import Country,State,City,Place
from django.contrib.auth.models import User
from django.core import serializers

class ConfigurationTestCase(TestCase):
    fixtures = ['auth.json']

    def setUp(self):
        Country.objects.create(name="Iran",initials="IR",code="+98",active=True)
        country=Country.objects.get(name="Iran")
        State.objects.create(name="Tehran",initials="TEH",code="21",active=True,country=country)
        pass

    def test_country(self):
        return
        data = {
            "name" : "Iraq",
            "initials": "IQ",
            "code" : "+97",
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
        countries = Country.objects.all()
        print(countries)
        for c in countries:
            print(c.name)

        country=Country.objects.get(name="Iran")
        data = {
            "name" : "Karaj",
            "code" : "026",
            "country": country.id,
            "initials": "KAR",
            "active" : True
        }
        client = APIClient()
        client.login(username='service', password='ser12345')
        print(f"{data}")
        response = client.post('/api/v1/location/state/', data, format='json')
        print(response.content)
        assert response.status_code == 201
        state = State.objects.get(name="Tehran")
        assert state != None

        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        response = client.post('/api/v1/location/state/', data, format='json')
        assert response.status_code == 403

    def test_city(self):
        return
        state_pk = State.objects.get(name="Tehran")

        data = {
            "name" : "Tehran",
            "state": f"{state_pk}",
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
        return
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
