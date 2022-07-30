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
router.register(r'vacancy/vacancy', views.VacancyViewSet, basename='vacancy')
router.register(r'vacancy/skill', views.SkillViewSet)
router.register(r'vacancy/category', views.CategoryViewSet)
router.register(r'vacancy/level', views.LevelViewSet)
router.register(r'vacancy/country', views.CountryViewSet)
router.register(r'vacancy/state', views.StateViewSet)
router.register(r'vacancy/city', views.CityViewSet)
router.register(r'vacancy/place', views.PlaceViewSet)
router.register(r'vacancy/estimate', views.EstimateViewSet)
