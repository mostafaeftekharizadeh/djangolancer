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
router.register(r'api/configuration/estimate', views.EstimateViewSet, basename='estimate')
router.register(r'api/configuration/profile_type', views.ProfileTypeViewSet, basename='profileType')
router.register(r'api/configuration/bank_name', views.BankNameViewSet, basename='bank_name')
router.register(r'api/configuration/language', views.LanguageViewSet, basename='language')
router.register(r'api/configuration/level', views.LevelViewSet, basename='level')
router.register(r'api/configuration/view_status', views.ViewStatusViewSet, basename='viewStatus')
router.register(r'api/configuration/currency', views.CurrencyViewSet, basename='currency')
router.register(r'api/configuration/status', views.StatusViewSet, basename='status')
router.register(r'api/configuration/work_category', views.WorkCategoryViewSet, basename='work_category')
router.register(r'api/configuration/skill', views.SkillViewSet, basename='Skill')
router.register(r'api/configuration/complain_type', views.ComplainTypeViewSet, basename='complain_type')
router.register(r'api/configuration/degree', views.DegreeViewSet, basename='degree')

urlpatterns = [
]
