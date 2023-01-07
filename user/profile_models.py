import os
import hashlib
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from library.models import BaseModel
from .user_models import Party
from location.models import City, State, Country
from configuration.models import ProfileType, Level, Degree, Language as BaseLanguage
from configuration.models import Skill as BaseSkill



class Profile(models.Model):
    def hash_upload(instance, filename):
        # delete old avatar if exists
        this = Profile.objects.get(party=instance.party)
        try:
            this.avatar.delete()
        except:
            pass
        fname, ext = os.path.splitext(filename)
        return "avatar/{0}{1}".format(hashlib.md5(fname.encode('utf-8')).hexdigest(), ext)
    party = models.OneToOneField(Party, primary_key=True, related_name="party_profile", unique=True, on_delete=models.CASCADE)
    date_birth = models.DateField(null=True,blank=True, auto_now=False, auto_now_add=False)
    avatar = models.ImageField(upload_to=hash_upload, null=True, blank=True)
    age = models.IntegerField(default=0,null=True, blank=True)
    about_me = models.TextField(default="",null=True, blank=True)
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



class Contact(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_contact')
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


class Skill(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_skill')
    skill = models.ForeignKey(BaseSkill, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('party', 'skill',)


class Job(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_job')
    title = models.TextField()
    company = models.TextField()
    description = models.TextField()
    date_start = models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)


class Education(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_education')
    degree = models.ForeignKey(Degree ,  on_delete=models.CASCADE)
    uni_name = models.TextField(default="")
    major = models.TextField(default="")
    date_start = models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)
    class Meta:
        unique_together = ('party', 'degree',)

class Certificate(BaseModel):
    party = models.ForeignKey(Party,  on_delete=models.CASCADE, related_name='party_certificate')
    name = models.TextField()
    description = models.TextField()
    Institution_name = models.TextField()
    date_start = models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)


class Specialty(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_speciality')
    name = models.TextField()
    level = models.TextField()
    description = models.TextField()
    Institution_name = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Achievement(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_achievement')
    title = models.TextField()
    event = models.TextField()
    description = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField( auto_now=False, auto_now_add=False)


class Language(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_language')
    language = models.ForeignKey(BaseLanguage, on_delete=models.CASCADE)
    talking = models.IntegerField(default=0, null=True, blank=True)
    writing = models.IntegerField(default=0, null=True, blank=True)
    comprehension = models.IntegerField(default=0, null=True, blank=True)

class WorkSample(BaseModel):
    def hash_upload(instance, filename):
        # delete old avatar if exists
        this = WorkSample.objects.get(party=instance.party)
        try:
            this.avatar.delete()
        except:
            pass
        fname, ext = os.path.splitext(filename)
        return "worksample/{0}{1}".format(hashlib.md5(fname.encode('utf-8')).hexdigest(), ext)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_worksample')
    title = models.TextField()
    skill = models.OneToOneField(BaseSkill, unique=True, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to=hash_upload, null=True, blank=True)

class Experience(BaseModel):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_experience')
    title = models.TextField()
    description = models.TextField()
    place = models.CharField(default="", max_length=255)
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)


class SocialMedia(BaseModel):
    party = models.ForeignKey(Party,  on_delete=models.CASCADE, related_name='party_socialmedia')
    name = models.TextField()
    userid = models.TextField()
    phone = models.TextField()
    link = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)

class Vote(BaseModel):
    party = models.OneToOneField(Party, related_name="vote_party", unique=True, on_delete=models.CASCADE)
    owner = models.OneToOneField(Party, related_name="vote_owner", unique=True, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0, null=True, blank=True)

