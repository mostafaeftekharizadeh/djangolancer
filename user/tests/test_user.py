from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user.models import Party
import json


# Create your tests here.
class UserTestCase(TestCase):
    fixtures = ['auth.json', 'location.json', 'configuration.json', 'user.json']

    def setUp(self):
        pass

    def test_register(self):
        client = APIClient()
        data = {
            "username" : "testuser",
            "password" : "arian1391",
            "password2" : "arian1391",
            "email" : "testuser@midlancer.ir",
            "first_name" : "fname1",
            "last_name" : "lname1"
        }
        response = client.post('/api/v1/user/user/', data, format='json')
        assert response.status_code == 201
        party = Party.objects.get(user__username="testuser")
        assert party != None

    def test_login(self):
        client = APIClient()
        data = {
	        "username" : "testuser1",
	        "password" : "testuser1"
        }
        response = client.post('/api/v1/user/login/', data, format='json')
        assert response.status_code == 200

    def test_user_list(self):
        client = APIClient()
        response = client.get('/api/v1/user/user/')
        data = json.loads(response.content)
        assert response.status_code == 200
        self.assertEqual(len(data['results']), 10)

    def test_user_delete(self):
        user = User.objects.get(username='testuser7')
        client = APIClient()
        client.login(username='testuser7', password='testuser7')
        response = client.delete('/api/v1/user/user/7/')
        assert response.status_code == 204

