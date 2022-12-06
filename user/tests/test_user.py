from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user.models import Party, Otp
import json


class UserTestCase(TestCase):
    fixtures = ['auth.json', 'location.json', 'configuration.json', 'user.json']

    def setUp(self):
        self.new_user_data = {
            "username" : "testuser",
            "password" : "arian1391",
            "password2" : "arian1391",
            "email" : "testuser@midlancer.ir",
            "first_name" : "fname1",
            "last_name" : "lname1"
        }
        pass

    def test_register(self):
        client = APIClient()
        response = client.post('/api/v1/user/user/', self.new_user_data, format='json')
        assert response.status_code == 201
        party = Party.objects.get(user__username="testuser")
        assert party != None
        user = User.objects.get(username="testuser")
        assert user.is_active == False

    def test_login(self):
        client = APIClient()
        data = {
	        "username" : "testuser1",
	        "password" : "testuser1"
        }
        response = client.post('/api/v1/user/login/', data, format='json')
        assert response.status_code == 200

    def test_login_not_active_user(self):
        client = APIClient()
        response = client.post('/api/v1/user/user/', self.new_user_data, format='json')
        client = APIClient()
        data = {
	        "username" : "testuser",
	        "password" : "testuser"
        }
        response = client.post('/api/v1/user/login/', data, format='json')
        assert response.status_code == 400

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

    def test_otp(self):
        client = APIClient()
        # register new user
        response = client.post('/api/v1/user/user/', self.new_user_data, format='json')
        user_data = json.loads(response.content)
        # request for otp
        data = {
            "token" : user_data['token']
        }
        response = client.post('/api/v1/user/otp/', data)
        assert response.status_code == 201
        # otp rate limit check
        response = client.post('/api/v1/user/otp/', data)
        assert response.status_code == 400
        otp = Otp.objects.get(user__username=user_data['username'])
        # otp confirm
        data = {
            'token' : user_data['token'],
            'code' : otp.code
        }
        response = client.post('/api/v1/user/otp/', data)
        assert response.status_code == 201
        user = User.objects.get(username=user_data['username'])
        assert user.is_active == True
        # otp expires after first use
        response = client.post('/api/v1/user/otp/', data)
        assert response.status_code == 400






