from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path

from . import settings
import importlib



router = routers.DefaultRouter()



schema_view = get_schema_view(
   openapi.Info(
      title="Midlancer API",
      default_version='v1',
      description="",
      #terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@midlancer.ir"),
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]

'''
automatically add apps url patterns
'''
for app in settings.MIDLANCER_APPS:
    _app = importlib.import_module(app + ".urls")
    urlpatterns += _app.urlpatterns
    router.registry.extend(_app.router.registry)

urlpatterns += [
    re_path(r'api/v1/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
