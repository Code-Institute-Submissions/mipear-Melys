from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Workshops(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
      return self.name

class WorkshopApply(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    reason = models.TextField(max_length=500)
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
      return self.name