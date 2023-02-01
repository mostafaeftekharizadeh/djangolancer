"""
Location test Case
"""
from django.test import TestCase
from rest_framework.test import APIClient
from location.models import Country, State, City, Place


class ConfigurationTestCase(TestCase):
    """
    Location Test case class
    """

    fixtures = ["auth.json"]

    def setUp(self):
        Country.objects.create(name="Iran", initials="IR", code="+98", active=True)
        country = Country.objects.get(name="Iran")
        State.objects.create(
            name="Tehran", initials="TEH", code="21", active=True, country=country
        )

    def test_country(self):
        """
        Country Test
        """
        # return
        data = {"name": "Iraq", "initials": "IQ", "code": "+97", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/location/country/", data, format="json")
        assert response.status_code == 201
        country = Country.objects.get(name="Iran")
        assert country is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/location/country/", data, format="json")
        assert response.status_code == 403

    def test_state(self):
        """
        State Test
        """
        country = Country.objects.get(name="Iran")
        data = {
            "name": "Karaj",
            "code": "026",
            "country": country.id,
            "initials": "KAR",
            "active": True,
        }
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/location/state/", data, format="json")
        assert response.status_code == 201
        # irint(response.content)
        state = State.objects.get(name="Tehran")
        assert state is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/location/state/", data, format="json")
        assert response.status_code == 403

    def test_city(self):
        """
        City Test
        """
        # return
        state_pk = State.objects.get(name="Tehran")

        data = {"name": "Tehran", "state": f"{state_pk}", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/location/city/", data, format="json")
        assert response.status_code == 201
        city = City.objects.get(name="Tehran")
        assert city is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/location/city/", data, format="json")
        assert response.status_code == 403

    def test_place(self):
        """
        Place Test
        """
        # return
        data = {"name": "InOffice", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/location/place/", data, format="json")
        assert response.status_code == 201
        place = Place.objects.get(name="InOffice")
        assert place is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/location/place/", data, format="json")
        assert response.status_code == 403
