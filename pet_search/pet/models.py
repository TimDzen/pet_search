from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.forms import forms



class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, verbose_name='Кличка')
    species = models.ForeignKey('Species', on_delete=models.PROTECT, to_field='id',verbose_name='Разновидность')
    age = models.IntegerField(verbose_name='Возраст')
    gender = models.CharField(max_length=20, verbose_name='Пол')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    location = models.CharField(max_length=255, verbose_name='Место')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    lost = models.BooleanField(default=True, verbose_name='Потерян?')
    photo = models.ImageField(upload_to='images/', default=None, blank=True, null=True, verbose_name='Добавить фото')

    class Meta:
        verbose_name = 'Животные'
        verbose_name_plural = 'Животные'


class Species(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Разновидность'
        verbose_name_plural = 'Разновидность'

    def __str__(self):
        return self.name
