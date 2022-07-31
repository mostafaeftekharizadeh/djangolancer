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
    try:
        _app = importlib.import_module(app + ".urls")
        try:
            urlpatterns += _app.urlpatterns
        except:
            pass
        try:
            router.registry.extend(_app.router.registry)
        except:
            pass
    except:
        pass

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
