import os
import binascii
import random
import hashlib
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from library.models import BaseModel


class UserManager(BaseUserManager):
    """
    Custom user model manager where mobile is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, mobile, password, **extra_fields):
        """
        Create and save a User with the given mobile and password.
        """
        if not mobile:
            raise ValueError(_('The Mobile must be set'))
        #mobile = self.normalize_mobile(mobile)
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobile, password, **extra_fields):
        """
        Create and save a SuperUser with the given mobile and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(mobile, password, **extra_fields)

class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    mobile = models.CharField(_('mobile number'), max_length=12, unique=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.mobile

class Party(BaseModel):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    owner = models.OneToOneField('self', related_name="party_owner", null=True, blank=True, on_delete=models.CASCADE)
    deleted_date = models.DateTimeField(null=True,blank=True)

class Otp(models.Model):
    mobile = models.CharField(max_length=12, blank=False, null=False )
    code = models.CharField(max_length=255, blank=False, null=False )
    token = models.CharField(default='', max_length=255, blank=False, null=False )
    created_at = models.DateTimeField(default=timezone.now)
    activated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.token = self.generate_token()
        if not self.code:
            self.code = self.generate_code()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_token(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    @classmethod
    def generate_code(cls):
        return random.randint(10000, 99999)
