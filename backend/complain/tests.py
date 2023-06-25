"""
Complain test Case
"""
from django.test import TestCase
from rest_framework.test import APIClient
from complain.models import Complain, ResultComplain
from rest_framework import status


class ComplainTestCase(TestCase):
    """
    Complain Test case class
    """

    fixtures = ["user.json", "level.json", "category.json", "skill.json"]

    # def test_complain(self):
        # """
        # Complain post Test
        # """
        # client = APIClient()
        # client.login(username="989120000010", password="1")
        # response = client.post("/api/v1/complain/complain/",data={ "description":"TEST_Des"}, format="json")
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # response = client.get("/api/v1/complain/complain" + str(place.id) + "/")
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_resultComplain(self):
    #     """
    #     Country Test
    #     """
    #     Country.objects.create(name="Iran", initials="IR", code="+98", active=True)
    #     country = Country.objects.get(name="Iran")
    #     assert country is not None
    #     client = APIClient()
    #     client.login(username="989120000010", password="1")
    #     response = client.get("/api/v1/complain/resultComplain", format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     response = client.get("/api/v1/complain/resultComplain" + str(country.id) + "/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
