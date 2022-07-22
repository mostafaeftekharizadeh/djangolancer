from django.db import models
from django.contrib.auth.models import User
from location.models import Country, State, City, Place
from configuration.models import Estimate

class Skill(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    time_estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    expire_date = models.DateTimeField()
    budget_total = models.IntegerField()
    budget_min = models.IntegerField()
    budget_max = models.IntegerField()
    deposit = models.IntegerField()
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Cost(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    calculate_cost = models.IntegerField()
    pay_cost = models.IntegerField()
    date = models.DateTimeField()


class Applicant(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.IntegerField()
    time = models.IntegerField()
    def __str__(self):
        return self.description

class ApplicantLevel(models.Model): 
    Applicant =  models.ForeignKey(Applicant, on_delete=models.CASCADE)  
    title = models.TextField()
    time = models.IntegerField()
    optional = models.BooleanField()
    cost = models.IntegerField()    
    def __str__(self):
        return self.title
