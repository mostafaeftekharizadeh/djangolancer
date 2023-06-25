"""
Chat test Case
"""
from django.test import TestCase
from rest_framework.test import APIClient
from chat.models import Room ,Participate,Message
from rest_framework import status


class ChatTestCase(TestCase):
    """
    Location Test case class
    """

    fixtures = ["user.json", "level.json", "category.json", "skill.json"]

    def test_chat_room(self):
        """
        Place Test
        """
        Place.objects.create(name="InHome", active=True)
        place = Place.objects.get(name="InHome")
        assert place is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/chat/room", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get("/api/v1/chat/room" + str(place.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chat_participate(self):
        """
        Country Test
        """
        Country.objects.create(name="Iran", initials="IR", code="+98", active=True)
        country = Country.objects.get(name="Iran")
        assert country is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/chat/participate", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get("/api/v1/chat/participate" + str(country.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_chatroom_message(self):
        """
        Country Test
        """
        Country.objects.create(name="Iran", initials="IR", code="+98", active=True)
        country = Country.objects.get(name="Iran")
        assert country is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/chat/message/"+ID, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get("/api/v1/chat/message/"+ID + str(country.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)