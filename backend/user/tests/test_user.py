"""
userTest unit
"""
import json
from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from user.user_models import Party, Otp


User = get_user_model()


class UserTestCase(TestCase):
    # fixtures = ['auth.json', 'location.json', 'configuration.json', 'user.json']
    fixtures = ["user.json"]

    def setUp(self):
        self.new_user_data = {
            "username": "testuser",
            "password": "arian1391",
            "password2": "arian1391",
            "mobile": "989121000001",
            "first_name": "fname1",
            "last_name": "lname1",
        }
        settings.DEBUG = True
        pass

    def test_register(self):
        client = APIClient()
        response = client.post("/api/v1/user/user/", self.new_user_data, format="json")
        otp_data = json.loads(response.content)
        assert response.status_code == 201
        data = {
            "token": otp_data["otp_token"],
            "mobile": self.new_user_data["mobile"],
            "code": "12345",
        }
        response = client.post("/api/v1/user/otp/", data)
        otp_data = json.loads(response.content)
        self.new_user_data["otp_token"] = otp_data["token"]
        response = client.post("/api/v1/user/user/", self.new_user_data, format="json")
        party = Party.objects.get(user__username="testuser")
        assert party != None

    def test_login(self):
        client = APIClient()
        data = {"mobile": "09120000001", "password": "1"}
        response = client.post("/api/v1/user/login/", data, format="json")
        assert response.status_code == 200

    def test_login_not_active_user(self):
        client = APIClient()
        response = client.post("/api/v1/user/user/", self.new_user_data, format="json")
        client = APIClient()
        data = {"username": "testuser", "password": "testuser"}
        response = client.post("/api/v1/user/login/", data, format="json")
        assert response.status_code == 400

    def test_user_list(self):
        client = APIClient()
        response = client.get("/api/v1/user/user/")
        data = json.loads(response.content)
        assert response.status_code == 200
        self.assertEqual(len(data["results"]), 10)

    def test_otp(self):
        client = APIClient()
        # register new user
        response = client.post("/api/v1/user/user/", self.new_user_data, format="json")
        user_data = json.loads(response.content)

        # otp confirm
        otp = Otp.objects.get(mobile=self.new_user_data["mobile"])

        data = {
            "mobile": self.new_user_data["mobile"],
            "token": user_data["otp_token"],
            "code": otp.code,
        }
        response = client.post("/api/v1/user/otp/", data)
        assert response.status_code == 201
        user = User.objects.get(mobile="989120000014")
        assert user.is_active is True
        response = client.post("/api/v1/user/otp/", data)
        assert response.status_code == 400

    def test_party(self):
        client = APIClient()
        response = client.get("/api/v1/user/party/")
        assert response.status_code == 200
