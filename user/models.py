from django.db import models
from django.contrib.auth.models import User
from location.models import City, State, Country
from configuration.models import ProfileType, Level, Degree, Language as BaseLanguage
from configuration.models import Skill as BaseSkill
from datetime import datetime


class Party(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    owner = models.OneToOneField('self', related_name="party_owner", null=True, blank=True, on_delete=models.CASCADE)
    deleted_date = models.DateTimeField(null=True,blank=True)


class Profile(models.Model):
    party = models.OneToOneField(Party, related_name="party_profile", unique=True, on_delete=models.CASCADE)
    date_birth = models.DateField(null=True,blank=True, auto_now=False, auto_now_add=False)
    age = models.IntegerField(default=0,null=True, blank=True)
    GENDER_CHOICES = [
        ("f", 'Female'),
        ("m", 'Male'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='m',
        null=True, blank=True
    )
    MARITAL_CHOICES = [
        ("y", 'Yes'),
        ("n", 'No'),
    ]
    marital = models.CharField(
        max_length=1,
        choices=MARITAL_CHOICES,
        default='m',
        null=True, blank=True
    )
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    panel = models.IntegerField(default=0,null=True, blank=True)
    panel_timeout = models.DateTimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=False)
    news = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True, blank=True)


class Contact(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    CONTACT_TYPE_CHOICES = [
        ("p", 'Phone'),
        ("m", 'Mobile'),
        ("a", 'Address'),
    ]
    contact_type = models.CharField(
        max_length=1,
        choices=CONTACT_TYPE_CHOICES,
        default='a',
        null=True, blank=True
    )
    contact = models.TextField()


class Skill(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_skill')
    skill = models.ForeignKey(BaseSkill, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('party', 'skill',)


class Job(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_job')
    title = models.TextField()
    company = models.TextField()
    description = models.TextField()
    date_start = models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)


class Education(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_education')
    degree = models.OneToOneField(Degree , unique=True, on_delete=models.CASCADE)
    uni_name = models.TextField()
    description = models.TextField()
    date_start = models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)

class Certificate(models.Model):
    party = models.ForeignKey(Party,  on_delete=models.CASCADE, related_name='party_certificate')
    name = models.TextField()
    description = models.TextField()
    Institution_name = models.TextField()
    date_start = models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)


class Specialty(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_speciality')
    name = models.TextField()
    level = models.TextField()
    description = models.TextField()
    Institution_name = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Achievement(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_achievement')
    title = models.TextField()
    event = models.TextField()
    description = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)


class Language(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_language')
    language = models.ForeignKey(BaseLanguage, on_delete=models.CASCADE)
    talking = models.IntegerField(default=0, null=True, blank=True)
    writing = models.IntegerField(default=0, null=True, blank=True)
    comprehension = models.IntegerField(default=0, null=True, blank=True)


class WorkSample(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_worksample')
    title = models.TextField()
    skill = models.OneToOneField(BaseSkill, unique=True, on_delete=models.CASCADE)
    description = models.TextField()


class SocialMedia(models.Model):
    party = models.ForeignKey(Party,  on_delete=models.CASCADE, related_name='party_socialmedia')
    name = models.TextField()
    userid = models.TextField()
    phone = models.TextField()
    link = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Vote(models.Model):
    party = models.OneToOneField(Party, related_name="vote_party", unique=True, on_delete=models.CASCADE)
    owner = models.OneToOneField(Party, related_name="vote_owner", unique=True, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0, null=True, blank=True)

