"""
configuration test module
"""
from django.test import TestCase
from rest_framework.test import APIClient
from configuration.models import (
    Bank,
    Category,
    ComplainType,
    Currency,
    Degree,
    Estimate,
    Language,
    ProfileType,
    Level,
    Skill,
    Status,
    ViewStatus,
)


class ConfigurationTestCase(TestCase):
    """
    configuration test case
    """

    fixtures = ["auth.json"]

    def setUp(self):
        pass

    def test_bank(self):
        """
        configuration bank test case
        """
        data = {"name": "test bank", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/bank/", data, format="json")
        assert response.status_code == 201
        bank = Bank.objects.get(name="test bank")
        assert bank is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/bank/", data, format="json")
        assert response.status_code == 403

    def test_category(self):
        """
        configuration category test case
        """
        data = {"name": "test category", "type": "w", "parent": "", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/category/", data, format="json")
        assert response.status_code == 201
        category = Category.objects.get(name="test category")
        assert category is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/category/", data, format="json")
        assert response.status_code == 403

    def test_complain_type(self):
        """
        configuration Complain Type test case
        """
        data = {"name": "test Complain_Type", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post(
            "/api/v1/configuration/complain_type/", data, format="json"
        )
        assert response.status_code == 201
        complain_type = ComplainType.objects.get(name="test Complain_Type")
        assert complain_type is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post(
            "/api/v1/configuration/complain_type/", data, format="json"
        )
        assert response.status_code == 403

    def test_currency(self):
        """
        configuration currency test case
        """
        data = {"name": "test currency", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/currency/", data, format="json")
        assert response.status_code == 201
        currency = Currency.objects.get(name="test currency")
        assert currency is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/currency/", data, format="json")
        assert response.status_code == 403

    def test_degree(self):
        """
        configuration degree test case
        """
        data = {"name": "test degree", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/degree/", data, format="json")
        assert response.status_code == 201
        degree = Degree.objects.get(name="test degree")
        assert degree is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/degree/", data, format="json")
        assert response.status_code == 403

    def test_estimate(self):
        """
        configuration estimate test case
        """
        data = {"name": "test estimate", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/estimate/", data, format="json")
        assert response.status_code == 201
        estimate = Estimate.objects.get(name="test estimate")
        assert estimate is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/estimate/", data, format="json")
        assert response.status_code == 403

    def test_language(self):
        """
        configuration language test case
        """
        data = {"name": "test language", "symbol": "TL", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/language/", data, format="json")
        assert response.status_code == 201
        language = Language.objects.get(name="test language")
        assert language is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/language/", data, format="json")
        assert response.status_code == 403

    def test_level(self):
        """
        configuration level test case
        """
        data = {"name": "test level", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/level/", data, format="json")
        assert response.status_code == 201
        level = Level.objects.get(name="test level")
        assert level is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/level/", data, format="json")
        assert response.status_code == 403

    def test_profile_type(self):
        """
        configuration language test case
        """
        data = {"name": "test profile_type", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post(
            "/api/v1/configuration/profile_type/", data, format="json"
        )
        assert response.status_code == 201
        profile_type = ProfileType.objects.get(name="test profile_type")
        assert profile_type is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post(
            "/api/v1/configuration/profile_type/", data, format="json"
        )
        assert response.status_code == 403

    def test_skill(self):
        """
        configuration skill test case
        """
        data = {
            # "category" : NULL,
            "name": "test skill",
            "active": True,
        }
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/skill/", data, format="json")
        assert response.status_code == 201
        skill = Skill.objects.get(name="test skill")
        assert skill is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/skill/", data, format="json")
        assert response.status_code == 403

    def test_status(self):
        """
        configuration status test case
        """
        data = {"name": "test status", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post("/api/v1/configuration/status/", data, format="json")
        assert response.status_code == 201
        status = Status.objects.get(name="test status")
        assert status is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post("/api/v1/configuration/status/", data, format="json")
        assert response.status_code == 403

    def test_view_status(self):
        """
        configuration view status test case
        """
        data = {"name": "test view_status", "active": True}
        client = APIClient()
        client.login(username="service", password="ser12345")
        response = client.post(
            "/api/v1/configuration/view_status/", data, format="json"
        )
        assert response.status_code == 201
        view_status = ViewStatus.objects.get(name="test view_status")
        assert view_status is not None

        client = APIClient()
        client.login(username="testuser1", password="testuser1")
        response = client.post(
            "/api/v1/configuration/view_status/", data, format="json"
        )
        assert response.status_code == 403

    # def test_work_category(self):
    #     data = {
    #         "name" : "test work_category",
    #         "active" : True
    #     }
    #     client = APIClient()
    #     client.login(username='service', password='ser12345')
    #     response = client.post('/api/v1/configuration/work_category/', data, format='json')
    #     assert response.status_code == 201
    #     work_category = work_category.objects.get(name="test work_category")
    #     assert work_category is not None

    #     client = APIClient()
    #     client.login(username='testuser1', password='testuser1')
    #     response = client.post('/api/v1/configuration/work_category/', data, format='json')
    #     assert response.status_code == 403

    # def test_site(self):
    #     data = {
    #         "name" : "test site",
    #         "active" : True
    #     }
    #     client = APIClient()
    #     client.login(username='service', password='ser12345')
    #     response = client.post('/api/v1/configuration/site/', data, format='json')
    #     assert response.status_code == 201
    #     site = Site.objects.get(name="test site")
    #     assert site is not None

    #     client = APIClient()
    #     client.login(username='testuser1', password='testuser1')
    #     response = client.post('/api/v1/configuration/site/', data, format='json')
    #     assert response.status_code == 403
