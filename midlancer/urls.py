from django.urls import include, path
from django.contrib import admin
from rest_framework import routers


from . import settings
import importlib



router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
]

'''
automatically add apps url patterns
'''
for app in settings.MIDLANCER_APPS:
    _app = importlib.import_module(app + ".urls")
    urlpatterns += _app.urlpatterns
    router.registry.extend(_app.router.registry)

print(urlpatterns)
urlpatterns += [
    path('', include(router.urls)),
]
