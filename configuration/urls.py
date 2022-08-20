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
router.register(r'configuration/Estimate', views.EstimateViewSet, basename='Estimate')
router.register(r'configuration/ProfileType', views.ProfileTypeViewSet, basename='ProfileType')
router.register(r'configuration/BankName', views.BankNameViewSet, basename='BankName')
router.register(r'configuration/Language', views.LanguageViewSet, basename='Language')
router.register(r'configuration/Level', views.LevelViewSet, basename='Level')
router.register(r'configuration/ViewStatus', views.ViewStatusViewSet, basename='ViewStatus')
router.register(r'configuration/Currency', views.CurrencyViewSet, basename='Currency')
router.register(r'configuration/Status', views.StatusViewSet, basename='Status')
router.register(r'configuration/WorkCategory', views.WorkCategoryViewSet, basename='WorkCategory')
router.register(r'configuration/Skill', views.SkillViewSet, basename='Skill')
router.register(r'configuration/ComplainType', views.ComplainTypeViewSet, basename='ComplainType')
router.register(r'configuration/Degree', views.DegreeViewSet, basename='Degree')

urlpatterns = [
]
