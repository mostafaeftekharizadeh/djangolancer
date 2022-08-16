from django.db import models
from django.contrib.auth.models import User
from location.models import City,State,Country
from configuration.models import ProfileType,Skill,Level,Degree,Language
# Create your models here.
class Maintainer(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
class UserRegister(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    phone_number=models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True, blank=True)
    address =models.TextField()
    






    
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    profile_type=models.ForeignKey(ProfileType, on_delete=models.CASCADE,null=True, blank=True)
    date_birth=models.DateField( auto_now=False, auto_now_add=False)
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
    vote_total= models.IntegerField(default=0,null=True, blank=True)

    
    
    panel=models.IntegerField(default=0,null=True, blank=True)
    panel_timeout=models.DateTimeField( auto_now=False, auto_now_add=False)
    active=models.BooleanField()
    news=models.BooleanField()
    def __str__(self):
        return self.user.username



class profile_skills():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)
    skill=models.OneToOneField(Skill, unique=True, on_delete=models.CASCADE)
    level=models.OneToOneField(Level, unique=True, on_delete=models.CASCADE)    

class profile_jobs():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)
    title=models.TextField()
    company=models.TextField()
    description=models.TextField()
    date_start=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end=models.DateTimeField( auto_now=False, auto_now_add=False)

class Education():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)  
    degree = models.OneToOneField(Degree , unique=True, on_delete=models.CASCADE) 
    uni_name=models.TextField()
    description=models.TextField()
    date_start=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end=models.DateTimeField( auto_now=False, auto_now_add=False)

class Certificate():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)  
    name=models.TextField()
    description=models.TextField()
    Institution_name=models.TextField()
    date_start=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end=models.DateTimeField( auto_now=False, auto_now_add=False)

class Specialty():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)  
    name=models.TextField()
    level=models.TextField()
    description=models.TextField()
    Institution_name=models.TextField()
    date_start=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end=models.DateTimeField( auto_now=False, auto_now_add=False)

class Achievement():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)  
    title=models.TextField()
    event=models.TextField()
    description=models.TextField()
    date_start=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end=models.DateTimeField( auto_now=False, auto_now_add=False)

class ProfileLanguage():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)  
    language=models.OneToOneField(Language, unique=True, on_delete=models.CASCADE)  
    talking= models.IntegerField(default=0,null=True, blank=True)
    writing= models.IntegerField(default=0,null=True, blank=True)
    comprehension= models.IntegerField(default=0,null=True, blank=True)

class WorkSample():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)  
    title=models.TextField()
    skill=models.OneToOneField(Skill, unique=True, on_delete=models.CASCADE)
    # w_img=models.OneToOneField(File_upload, unique=True, on_delete=models.CASCADE)  
    # thumbnail =models.OneToOneField(File_upload, unique=True, on_delete=models.CASCADE)  
    # file =models.OneToOneField(File_upload, unique=True, on_delete=models.CASCADE)  
    description=models.TextField()

class SocialMedia():
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE) 
    name=models.TextField()
    userid=models.TextField()
    phone=models.TextField()
    link=models.TextField()
    date_start=models.DateTimeField( auto_now=False, auto_now_add=False)
    date_end=models.DateTimeField( auto_now=False, auto_now_add=False)

class voting():
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE) 
    voter = models.OneToOneField(User, unique=True, on_delete=models.CASCADE) 		
    vot= models.IntegerField(default=0,null=True, blank=True)			

    
# class RegisterUser(models.Model):
#     user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)

#     city = models.ForeignKey(City, on_delete=models.CASCADE,null=True, blank=True)
#     GENDER_CHOICES = [
#         ("f", 'Female'),
#         ("m", 'male'),
#     ]
#     gender = models.CharField(
#         max_length=1,
#         choices=GENDER_CHOICES,
#         default='m',
#         null=True, blank=True
#     )
#     age = models.IntegerField(default=0,null=True, blank=True)
#     def __str__(self):
#         return self.user.username
