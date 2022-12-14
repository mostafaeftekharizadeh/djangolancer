from configuration.models import (Category, Currency, Estimate, Level, Skill as BaseSkill,
                                  Status)
from django.db import models
from location.models import City, Country, Place, State
from user.user_models import Party


class Project(models.Model):
    party = models.ForeignKey(Party ,on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, null=False, on_delete=models.CASCADE)
    work = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    # file_upload_img = models.ForeignKey(Profile,on_delete=models.CASCADE)
    skill = models.ManyToManyField(BaseSkill)
    exp_time = models.TimeField()
    description = models.TextField()
    # file_upload_des = models.ForeignKey(Profile,on_delete=models.CASCADE)
    currency = models.ForeignKey(
        Currency, null=False, on_delete=models.CASCADE)
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
    # cost = models.ForeignKey(Cost, on_delete=models.CASCADE)
    deleted_date = models.DateTimeField(null=True,blank=True)
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
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    total_level = models.IntegerField()
    total_time = models.IntegerField()
    total_price = models.IntegerField()
    promotion = models.IntegerField()
    description = models.TextField()
    state = models.BooleanField()

    def __str__(self):
        return self.description


class OfferLevel(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.IntegerField()
    optional = models.BooleanField()
    cost = models.IntegerField()

    def __str__(self):
        return self.title


class Budget(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    currency = models.ForeignKey(
        Currency, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.IntegerField()
    optional = models.BooleanField()
    cost = models.IntegerField()

    def __str__(self):
        return self.title
