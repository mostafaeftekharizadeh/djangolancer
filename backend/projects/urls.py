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

urlpatterns = []

router = routers.DefaultRouter()
router.register(r"project/project", views.ProjectViewSet, basename="project")
router.register(r"project/file", views.FileViewSet, basename="file")
router.register(
    r"project/filelist/(?P<project>[^/]+)", views.FileListViewSet, basename="filelist"
)
router.register(r"project/cost", views.CostViewSet, basename="cost")
router.register(
    r"project/offer/(?P<project>[^/]+)", views.OfferViewSet, basename="offer"
)
router.register(
    r"project/offer-detail/(?P<id>[^/]+)", views.OfferDeatilViewSet, basename="offer"
)
router.register(r"project/offer_step", views.OfferStepViewSet, basename="offer_step")
router.register(r"project/budget", views.BudgetViewSet, basename="budget")
router.register(r"project/test", views.NewViewSet, basename="test")
router.register(r"project/myoffer", views.MyOfferViewSet, basename="my_offer")
