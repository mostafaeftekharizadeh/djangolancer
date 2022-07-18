from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from user.urls import router as user_router
from vacancy.urls import router as vacancy_router
#from project.urls import router as project_router
from user.views import LoginView



router = routers.DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(vacancy_router.registry)
#router.registry.extend(project_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view()),
]
