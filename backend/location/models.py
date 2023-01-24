"""
Location Models
"""
from django.db import models
from library.models import BaseModel

# Create your models here.
class Country(BaseModel):
    """
    Country Serializers
    """

    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=3, default="")
    code = models.CharField(max_length=10, default="")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class State(BaseModel):
    """
    State Serializers
    """

    name = models.TextField()
    initials = models.CharField(max_length=3)
    code = models.CharField(max_length=10, default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class City(BaseModel):
    """
    City Serializers
    """

    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Place(BaseModel):
    """
    Place Serializers
    """

    name = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
