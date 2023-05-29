from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user.profile_models import Party, Profile, Skill
import json
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model


class ProfileTestCase(TestCase):
    # fixtures = ['auth.json', 'location.json', 'configuration.json', 'user.json']
    fixtures = ["user.json", "category.json", "level.json", "skill.json"]

    def setUp(self):
        pass

    def test_create_profile(self):
        User = get_user_model()
        user = User.objects.filter(mobile="989120000014")

        client = APIClient()
        client.login(username="989120000014", password="1")
        test_image = SimpleUploadedFile(
            "test_image.jpg", content=b"", content_type="image/jpg"
        )
        data = {
            "date_birth": "2022-11-05",
            "age": 50,
            "about_me": "I'm a test",
            "gender": "m",
            "marital": "y",
            "vote_total": 0,
            "panel": 0,
            "panel_timeout": "2022-11-05T16:18:48.543Z",
            "active": True,
            "news": True,
            "is_employer": True,
            # "country": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            # "state": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            # "city": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "avatar": test_image,
            # "party": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        }
        # profile must be created after user create
        response = client.post("/api/v1/user/profile/profile/", data, format="json")
        assert response.status_code == 400

        profile = Profile.objects.get(party=user[0].party)

        assert profile.party.user.username == "989120000014"

    def test_update_profile(self):
        client = APIClient()
        client.login(username="989120000014", password="1")
        data = {
            "date_birth": "2022-11-05",
            "age": 50,
        }
        response = client.put(
            "/api/v1/user/profile/profile/451a44ed-2f34-40ac-b808-b5a0f332c7ad/",
            data,
            format="json",
        )
        assert response.status_code == 200

        profile = Profile.objects.get(party="451a44ed-2f34-40ac-b808-b5a0f332c7ad")
        assert profile.age == 50

    def test_update_profile_permission(self):
        client = APIClient()
        client.login(username="989120000014", password="testuser3")

        data = {
            "date_birth": "2022-11-05",
            "age": 50,
            "gender": "m",
            "marital": "y",
            "vote_total": 0,
            "panel": 0,
            "panel_timeout": "2022-11-05T16:18:48.543Z",
            "active": True,
            "news": True,
            "country": 1,
            "state": 1,
            "city": 1,
        }

        response = client.put(
            "/api/v1/user/profile/profile/451a44ed-2f34-40ac-b808-b5a0f332c7ad/",
            data,
            format="json",
        )
        assert response.status_code == 401

    def test_add_skill(self):
        client = APIClient()
        client.login(username="989120000014", password="1")
        data = {
            "skill": "f8f72374-37cd-4b51-ae84-31849868cf00",
            "level": "68472fb1-f357-477b-9c05-2bcd44d31326",
        }
        # user can add skill
        response = client.post("/api/v1/user/profile/skill/", data, format="json")
        assert response.status_code == 201
        # user can delete his/him skill
        s = json.loads(response.content)
        url = "/api/v1/user/profile/skill/%s/" % (s["id"])
        response = client.delete(url, format="json")
        assert response.status_code == 204

        # user can add skill

        s = Skill.objects.filter(party__user__username="989120000010")
        assert len(s) == 0
        # user can't delete others skill
        url = "/api/v1/user/profile/skill/f8f72374-37cd-4b51-ae84-31849868cf00/"
        response = client.delete(url, format="json")
        assert response.status_code == 404
