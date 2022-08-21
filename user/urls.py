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
    path('api/user/login', views.LoginView.as_view(), name='login_view'),
    path('api/user/password', views.ChangePasswordView.as_view(), name='change_password_view'),
    path('api/user/update', views.UpdateUserView.as_view(), name='update_user_view'),
    path('api/user/Profile', views.ProfileViewSet, name='Profile'),
    path('api/user/Profile_skills', views.Profile_skillsViewSet, name='profile_skills'),
    path('api/user/Profile_jobs', views.Profile_jobsViewSet, name='profile_jobs'),
    path('api/user/Education', views.EducationViewSet, name='Education'),
    path('api/user/Certificate', views.CertificateViewSet, name='Certificate'),
    path('api/user/Specialty', views.SpecialtyViewSet, name='Specialty'),
    path('api/user/Achievement', views.AchievementViewSet, name='Achievement'),
    path('api/user/ProfileLanguage', views.ProfileLanguageViewSet, name='ProfileLanguage'),
    path('api/user/WorkSample', views.WorkSampleViewSet, name='WorkSample'),
    path('api/user/SocialMedia', views.SocialMediaViewSet, name='SocialMedia'),
    path('api/user/voting', views.VotingViewSet, name='voting'),
]


router = routers.DefaultRouter()
#router.register(r'user/maintainer', views.MaintainerViewSet)


