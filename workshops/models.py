from django.db import models

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