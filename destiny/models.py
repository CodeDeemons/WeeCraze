from django.db import models

# Create your models here.
class Destiny(models.Model):
    name = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    img_name = models.CharField(max_length=10)
    category = models.CharField(max_length=30)
    short_desc = models.CharField(max_length=300)
    long_desc = models.CharField(max_length=12000)