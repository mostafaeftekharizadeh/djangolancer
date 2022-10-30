from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


# Create your tests here.
class UserTestCase(TestCase):
    fixtures = ['users.json', 'auth.user']
    def setUp(self):
        pass

    def login(self):
        client = APIClient()
        data = {
	        "username" : "mid1",
	        "password" : "arian1391"
        }
        response = client.post('/api/v1/user/login/', data, format='json')

        assert response.status_code == 200

    def register(self):
        client = APIClient()
        data = {
            "username" : "mid1",
            "password" : "arian1391",
            "password2" : "arian1391",
            "email" : "mid1@midlancer.ir",
            "first_name" : "fname1",
            "last_name" : "lname1"
        }
        #response = client.post('/api/v1/user/user/', data, format='json')
        u = User.objects.get(username='mid1')
        #assert response.status_code == 201

    def test_1_register_new_user(self):
        self.register()
        self.login()


