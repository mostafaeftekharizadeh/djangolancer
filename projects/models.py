from django.db import models
from django.contrib.auth.models import User
from location.models import Country, State, City, Place
from configuration.models import Estimate, Status,WorkCategory
from user.models import Profile
from configuration.models import Skill,Status,Level

class Project(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    work = models.TextField()
    title = models.TextField()
    # file_upload_img = models.ForeignKey(Profile,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    exp_time = models.TextField()
    description = models.TextField()
    # file_upload_des = models.ForeignKey(Profile,on_delete=models.CASCADE)
    currency =  models.TextField()
    budget_min = models.IntegerField()
    budget_max = models.IntegerField()
    tag = models.TextField()
    cre_price = models.IntegerField()
    budget_total = models.IntegerField()
    expire_date = models.DateTimeField(null=True, blank=True)
    discount = models.IntegerField()
    date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    cost = models.ForeignKey(Cost, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #file_upload = models.ForeignKey(Profile,on_delete=models.CASCADE)
class Cost(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    calculate_cost = models.IntegerField()
    pay_cost = models.IntegerField()
    pay_date = models.DateTimeField()
class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    total_level = models.IntegerField()
    total_time = models.IntegerField()
    total_price = models.IntegerField()
    promotion = models.IntegerField()
    description = models.TextField()
    state = models.BooleanField()
    def __str__(self):
        return self.description
class OfferLevel(models.Model):
    offer =  models.ForeignKey(Offer, on_delete=models.CASCADE)
    title = models.TextField()
    time = models.IntegerField()
    optional = models.BooleanField()
    cost = models.IntegerField()
    def __str__(self):
        return self.title
class Budget(models.Model):
    project =  models.ForeignKey(Project, on_delete=models.CASCADE)
    currency = models.TextField()
    title = models.TextField()
    time = models.IntegerField()
    optional = models.BooleanField()
    cost = models.IntegerField()
    def __str__(self):
        return self.title
