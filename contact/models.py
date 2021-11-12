from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    adress = models.CharField(max_length=80)
    message = models.CharField(max_length=200)