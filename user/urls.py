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


urlpatterns = [
    path('api/user/register', views.UserRegisterView.as_view(), name='auth_register'),
    path('api/user/refresh', views.RefreshView.as_view(), name='auth_register'),
    path('api/user/verify', views.VerifyView.as_view(), name='auth_register'),
    path('api/user/login', views.LoginView.as_view(), name='login_view'),
    path('api/user/password', views.ChangePasswordView.as_view(), name='change_password_view'),
    path('api/user/update', views.UpdateUserView.as_view(), name='update_user_view'),
    path('api/user/profile', views.ProfileViewSet, name='profile'),
    path('api/user/profile_skills', views.Profile_skillsViewSet, name='profile_skills'),
    path('api/user/profile_jobs', views.Profile_jobsViewSet, name='profile_jobs'),
    path('api/user/education', views.EducationViewSet, name='education'),
    path('api/user/certificate', views.CertificateViewSet, name='certificate'),
    path('api/user/specialty', views.SpecialtyViewSet, name='specialty'),
    path('api/user/achievement', views.AchievementViewSet, name='achievement'),
    path('api/user/profile_language', views.ProfileLanguageViewSet, name='profile_language'),
    path('api/user/work_sample', views.WorkSampleViewSet, name='work_sample'),
    path('api/user/social_media', views.SocialMediaViewSet, name='social_media'),
    path('api/user/voting', views.VotingViewSet, name='voting'),
]


router = routers.DefaultRouter()
#router.register(r'user/maintainer', views.MaintainerViewSet)


