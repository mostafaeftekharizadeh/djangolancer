from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()
class MidlancerBackend(BaseBackend):
    def authenticate(self, request, mobile=None, password=None):
        try:
            user = User.objects.get(mobile=mobile)
        except:
            return
        if not user.is_active or not user.check_password(password):
            return
        return user

