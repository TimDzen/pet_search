from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    owner_contact = models.CharField(max_length=255)
    lost = models.BooleanField(default=True)

