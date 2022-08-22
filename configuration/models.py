from django.db import models

# Create your models here.
class Estimate(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class ProfileType(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class BankName(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class Language(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class Level(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class ViewStatus(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Currency(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Status(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.TextField()
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
    parent=models.ForeignKey('Category',on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name  
class Skill(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class ComplainType(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Degree(models.Model):
    name = models.TextField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name