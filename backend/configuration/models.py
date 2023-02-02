"""
Configurations model module
"""
from django.db import models
from library.models import BaseModel

# pylint: disable=too-many-ancestors
# Create your models here.
class Estimate(BaseModel):
    """
    Estimate model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProfileType(BaseModel):
    """
    Profile type model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Bank(BaseModel):
    """
    Bank model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Language(BaseModel):
    """
    Language model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    symbol = models.CharField(max_length=2, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Level(BaseModel):
    """
    Level model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ViewStatus(BaseModel):
    """
    View status model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Currency(BaseModel):
    """
    Currency model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Status(BaseModel):
    """
    Status model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    default = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(BaseModel):
    """
    Profile type model module
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    TYPE_CHOICES = [
        ("w", "Work"),
        ("p", "Parent"),
    ]
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default="w", null=True, blank=True
    )
    parent = models.ForeignKey(
        "Category", blank=True, null=True, on_delete=models.CASCADE
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Skill(BaseModel):
    """
    Skill model
    """

    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ComplainType(BaseModel):
    """
    Complain type model
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Degree(BaseModel):
    """
    Degree model module
    """

    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
