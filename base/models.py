from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField(max_length=50)
    lng = models.FloatField(max_length=50)
