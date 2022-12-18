from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from user.profile_models import Party, Profile, Skill
import json
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model


class ProfileTestCase(TestCase):
    # fixtures = ['auth.json', 'location.json', 'configuration.json', 'user.json']
    fixtures = ['compleated.json']
    

    def setUp(self):
        pass

    def test_create_profile(self):
        User = get_user_model()
        user = User.objects.filter(username='testuser3')
        print('-------------------------------------')
        print(user)
        print('-------------------------------------')
        client = APIClient()
        client.login(username='testuser3', password='testuser3')
        
        test_image = SimpleUploadedFile("test_image.jpg", "file_content", content_type="image/jpg")
        
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
            "about_me":"I'm a test",
            
            "avatar":test_image
        }
        response = client.post('/api/v1/user/profile/profile/', data, format='json')
        assert response.status_code == 201
        profile = Profile.objects.filter(party=user[0].party)



    def test_update_profile(self):
        client = APIClient()
        client.login(username='testuser1', password='testuser1')
        data = {
            "date_birth": "2022-11-05",
            "age": 50,
        }
        response = client.put('/api/v1/user/profile/profile/1/', data, format='json')
        assert response.status_code == 200

        profile = Profile.objects.get(party=1)
        assert profile.age == 50



    def test_update_profile_permission(self):
        client = APIClient()
        client.login(username='testuser3', password='testuser3')
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
            "city": 1
        }
        response = client.put('/api/v1/user/profile/profile/1/', data, format='json')
        assert response.status_code == 403

    def test_add_skill(self):
        client = APIClient()
        client.login(username='testuser3', password='testuser3')
        data = {
            "skill": 1,
            "level": 1
        }
        # user can add skill
        response = client.post('/api/v1/user/profile/skill/', data, format='json')
        assert response.status_code == 201
        # user can delete his/him skill
        s = json.loads(response.content)
        url = '/api/v1/user/profile/skill/%s/' % (s['id'])
        response = client.delete( url , format='json')
        assert response.status_code == 204
        s = Skill.objects.filter(party__user__username='testuser2')
        assert len(s) == 0
        # user can't delete others skill
        url = '/api/v1/user/profile/skill/1/'
        response = client.delete( url , format='json')
        assert response.status_code == 403





