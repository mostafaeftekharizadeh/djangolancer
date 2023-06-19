from django.urls import reverse

from rest_framework import status
from django.test import TestCase
from django.contrib import auth
from projects.models import Project

# from rest_framework.test import APITestCase


class ProjectViewSetTests(TestCase):
    fixtures = ["user.json", "level.json", "category.json", "skill.json"]

    def test_project_list_get(self):
        url = reverse("project-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_create_post(self):
        url = reverse("project-list")
        data = {
            "party": "451a44ed-2f34-40ac-b808-b5a0f332c7ad",
            "category": "c08e4130-4dba-4540-be36-459957f76761",
            "sub_category": "c9cac280-24c5-4126-afe9-2b8f730427e8",
            "title": "string",
            "description": "string",
            "skill": ["0129d54a-31ce-4afd-b719-f8acb67be527"],
            "duration": "12:20:30",
            "level": "68472fb1-f357-477b-9c05-2bcd44d31326",
            "budget_min": 100,
            "budget_max": 2000,
        }

        self.client.login(username="989120000014", password="1")
        user = auth.get_user(self.client)
        assert user.is_authenticated
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get created project
        pr = Project.objects.get(party="451a44ed-2f34-40ac-b808-b5a0f332c7ad")
        url = reverse("project-detail", kwargs={"pk": pr.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # update project
        url = reverse("project-detail", kwargs={"pk": pr.id})
        data = {
            "party": "451a44ed-2f34-40ac-b808-b5a0f332c7ad",
            "category": "c08e4130-4dba-4540-be36-459957f76761",
            "sub_category": "c9cac280-24c5-4126-afe9-2b8f730427e8",
            "title": "string2",
            "description": "string2",
            "skill": ["0129d54a-31ce-4afd-b719-f8acb67be527"],
            "duration": "12:20:30",
            "level": "68472fb1-f357-477b-9c05-2bcd44d31326",
            "budget_min": 100,
            "budget_max": 2000,
        }
        response = self.client.put(
            url, data, format="json", content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
