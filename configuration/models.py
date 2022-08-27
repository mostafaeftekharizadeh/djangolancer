from django.db import models

# Create your models here.
class Estimate(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class ProfileType(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class BankName(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class Language(models.Model):
    name = models.CharField(max_length=200)
    symbol=models.CharField(max_length=2,null=True)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class Level(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class ViewStatus(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Currency(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Status(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=200)
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
    parent=models.ForeignKey('Category',null=True,on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class Skill(models.Model):
    category= models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class ComplainType(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Degree(models.Model):
    name = models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name