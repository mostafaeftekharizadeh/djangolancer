from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.TextField()

class State(models.Model):
    name = models.TextField()
    initials = models.CharField(max_length=3)
    area_code = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    name = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Place(models.Model):
    name = models.TextField()

