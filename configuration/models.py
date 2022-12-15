from django.db import models
from library.models import BaseModel

# Create your models here.
class Estimate(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ProfileType(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Bank(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Language(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    symbol=models.CharField(max_length=2,null=True)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Level(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ViewStatus(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Currency(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Status(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    TYPE_CHOICES = [
        ("w", 'Work'),
        ("p", 'Parent'),
    ]
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default='w',
        null=True, blank=True
    )
    parent=models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Skill(BaseModel):
    category= models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ComplainType(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Degree(BaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
