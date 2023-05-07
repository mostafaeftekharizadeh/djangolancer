"""mitco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"configuration/site", views.SiteViewSet, basename="configutaion_site")
router.register(
    r"configuration/estimate", views.EstimateViewSet, basename="configutaion_estimate"
)
router.register(
    r"configuration/profile_type",
    views.ProfileTypeViewSet,
    basename="configuration_profile_type",
)
router.register(r"configuration/bank", views.BankViewSet, basename="configuration_bank")
router.register(
    r"configuration/language", views.LanguageViewSet, basename="configuration_language"
)
router.register(
    r"configuration/level", views.LevelViewSet, basename="configuration_level"
)
router.register(
    r"configuration/view_status",
    views.ViewStatusViewSet,
    basename="configuration_viewStatus",
)
router.register(
    r"configuration/currency", views.CurrencyViewSet, basename="configuration_currency"
)
router.register(
    r"configuration/status", views.StatusViewSet, basename="configuration_status"
)
router.register(
    r"configuration/work_category",
    views.CategoryViewSet,
    basename="configuration_work_category",
)
router.register(
    r"configuration/skill", views.SkillViewSet, basename="configuration_skill"
)
router.register(
    r"configuration/complain_type",
    views.ComplainTypeViewSet,
    basename="configuration_complain_type",
)
router.register(
    r"configuration/degree", views.DegreeViewSet, basename="configuration_degree"
)
router.register(
    r"configuration/category", views.CategoryViewSet, basename="configuration_category"
)
router.register(
    r"configuration/allcategory",
    views.AllCategoryViewSet,
    basename="configuration_all_category",
)
urlpatterns = []
