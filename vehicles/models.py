from django.db import models

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=10)
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=30)
    cc = models.CharField(max_length=10)
    milleage = models.CharField(max_length=10)
    type = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    img_name = models.CharField(max_length=20)