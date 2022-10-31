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
from . import views, profile_views


urlpatterns = [
    path('api/v1/user/login/', views.LoginView.as_view(), name='login_view'),
    path('api/v1/user/password/', views.ChangePasswordView.as_view(), name='change_password_view'),
    ### profile urls
    path('api/v1/user/profile/social_media/', profile_views.SocialMediaViewSet, name='social_media'),

    path('api/v1/user/vote/', views.VoteViewSet, name='vote'),
]


router = routers.DefaultRouter()
router.register(r'user/user', views.UserViewSet, basename='user')
router.register(r'user/party', views.PartyViewSet, basename='party')
router.register(r'user/profile/profile', profile_views.ProfileViewSet, basename='profile')
router.register(r'user/profile/skill', profile_views.SkillViewSet, basename='skill')
router.register(r'user/profile/job', profile_views.JobViewSet, basename='job')
router.register(r'user/profile/education', profile_views.EducationViewSet, basename='education')
router.register(r'user/profile/certificate', profile_views.CertificateViewSet, basename='certificate')
router.register(r'user/profile/specialty', profile_views.SpecialtyViewSet, basename='specialty')
router.register(r'user/profile/achievement', profile_views.AchievementViewSet, basename='achievement')
router.register(r'user/profile/language', profile_views.LanguageViewSet, basename='language')
router.register(r'user/profile/worksample', profile_views.WorkSampleViewSet, basename='worksample')
router.register(r'user/profile/socialmedia', profile_views.SocialMediaViewSet, basename='socialmedia')



