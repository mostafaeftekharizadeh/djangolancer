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
from rest_framework import status


class ConfigurationTestCase(TestCase):
    """
    configuration test case
    """

    # fixtures = ["auth.json"]

    # def setUp(self):
    #     pass

    fixtures = ["user.json", "level.json", "category.json", "skill.json"]

    def test_bank(self):
        """
        Bank Test
        """
        Bank.objects.create(name="TestBank", active=True)
        bank = Bank.objects.get(name="TestBank")
        assert bank is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/bank/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get("/api/v1/configuration/bank/" + str(bank.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category(self):
        """
        Category Test
        """
        Category.objects.create(name="TestCategory", active=True)
        category = Category.objects.get(name="TestCategory")
        assert category is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/category/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(
            "/api/v1/configuration/category/" + str(category.id) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_currency(self):
        """
        Currency Test
        """
        Currency.objects.create(name="TestCurrency", active=True)
        currency = Currency.objects.get(name="TestCurrency")
        assert currency is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/currency/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(
            "/api/v1/configuration/currency/" + str(currency.id) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_degree(self):
        """
        Degree Test
        """
        Degree.objects.create(name="TestDegre", active=True)
        degree = Degree.objects.get(name="TestDegre")
        assert degree is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/degree/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get("/api/v1/configuration/degree/" + str(degree.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_estimate(self):
        """
        Estimate Test
        """
        Estimate.objects.create(name="TestEstimate", active=True)
        estimate = Estimate.objects.get(name="TestEstimate")
        assert estimate is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/estimate/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(
            "/api/v1/configuration/estimate/" + str(estimate.id) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_language(self):
        """
        Language Test
        """
        Language.objects.create(name="Testlanguage", active=True)
        language = Language.objects.get(name="Testlanguage")
        assert language is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/language/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(
            "/api/v1/configuration/language/" + str(language.id) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_level(self):
        """
        Level Test
        """
        Level.objects.create(name="Testlevel", active=True)
        level = Level.objects.get(name="Testlevel")
        assert level is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/level/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get("/api/v1/configuration/level/" + str(level.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_type(self):
        """
        ProfileType Test
        """
        ProfileType.objects.create(name="Testprofile_type", active=True)
        profile_type = ProfileType.objects.get(name="Testprofile_type")
        assert profile_type is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/profile_type/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(
            "/api/v1/configuration/profile_type/" + str(profile_type.id) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status(self):
        """
        Status Test
        """
        Status.objects.create(name="Teststatus", default=False, active=True)
        status_obj = Status.objects.get(name="Teststatus")
        assert status_obj is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/status/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(
            "/api/v1/configuration/status/" + str(status_obj.id) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_skill(self):
        """
        Skill Test
        """
        Skill.objects.create(name="Testskill", active=True)
        skill = Skill.objects.get(name="Testskill")
        assert skill is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/skill/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get("/api/v1/configuration/skill/" + str(skill.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_status(self):
        """
        ViewStatus Test
        """
        ViewStatus.objects.create(name="TestViewStatus", active=True)
        view_status = ViewStatus.objects.get(name="TestViewStatus")
        assert view_status is not None
        client = APIClient()
        client.login(username="989120000010", password="1")
        response = client.get("/api/v1/configuration/view_status/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(
            "/api/v1/configuration/view_status/" + str(view_status.id) + "/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
