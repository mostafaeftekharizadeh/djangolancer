from django.db import models
from django.contrib.auth.models import User
from location.models import City

# Create your models here.
class Maintainer(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True, blank=True)
    GENDER_CHOICES = [
        ("f", 'Female'),
        ("m", 'male'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='m',
        null=True, blank=True
    )
    age = models.IntegerField(default=0,null=True, blank=True)
    def __str__(self):
        return self.user.username


