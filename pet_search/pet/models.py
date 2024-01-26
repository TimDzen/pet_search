from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.forms import forms

User = get_user_model()

class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    lost = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='images/', default=None, blank=True, null=True)



