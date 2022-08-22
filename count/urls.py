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
from django.urls import include, path
from rest_framework import routers
from . import views




router = routers.DefaultRouter()
router.register('api/count/count', views.CountViewSet, basename='count')
router.register('api/count/deposit', views.DepositViewSet, basename='deposit')
router.register('api/count/withdraw', views.WithdrawViewSet, basename='withdraw')
router.register('api/count/account', views.AccountViewSet, basename='account')
#router.register(r'user/maintainer', views.MaintainerViewSet)


urlpatterns = [
]