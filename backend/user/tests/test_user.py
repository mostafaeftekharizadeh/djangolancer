"""
userTest unit
"""
# import json
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from user.user_models import Party, Otp


User = get_user_model()


class UserTestCase(TestCase):
    # fixtures = ['auth.json', 'location.json', 'configuration.json', 'user.json']
    fixtures = ["compleated.json"]

    def setUp(self):
        self.new_user_data = {
            "username": "testuser",
            "password": "arian1391",
            "password2": "arian1391",
            "mobile": "989121000001",
            "first_name": "fname1",
            "last_name": "lname1",
        }
        pass

    def test_register(self):
        client = APIClient()
        response = client.post("/api/v1/user/user/", self.new_user_data, format="json")
        assert response.status_code == 201
        party = Party.objects.get(user__username="testuser")
        assert party != None
        user = User.objects.get(username="testuser")
        assert user.is_active == False

    def test_login(self):
        client = APIClient()
        data = {"username": "testuser1", "password": "testuser1"}
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

    def test_user_delete(self):
        user = User.objects.get(username="testuser7")
        client = APIClient()
        client.login(username="testuser7", password="testuser7")
        response = client.delete("/api/v1/user/user/7/")
        assert response.status_code == 204

    def test_otp(self):
        client = APIClient()
        # register new user
        response = client.post("/api/v1/user/user/", self.new_user_data, format="json")
        user_data = json.loads(response.content)
        # otp confirm
        otp = Otp.objects.get(user__username=user_data["username"])
        data = {"token": user_data["otp_token"], "code": otp.code}
        response = client.post("/api/v1/user/otp/", data)
        assert response.status_code == 201
        request_data = {"email": self.new_user_data["email"]}
        # otp rate limit check
        response_rate_limit = client.post("/api/v1/user/otp/", request_data)
        rate_limit_data = json.loads(response_rate_limit.content)
        assert rate_limit_data["no_feild_erros"] == "otp rate limit reached."
        # check if user is active after otp validation
        user = User.objects.get(username=user_data["username"])
        assert user.is_active is True
        # otp expires after first use
        response = client.post("/api/v1/user/otp/", data)
        assert response.status_code == 400
