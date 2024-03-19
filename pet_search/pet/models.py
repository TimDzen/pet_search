from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.forms import forms


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError(
            _('Номер телефона должен содержать только цифры.'),
            params={'value': value},
        )
    if len(value) > 11:
        raise ValidationError(
            _('Номер телефона не может быть длиннее 11 символов.'),
            params={'value': value},
        )
    raise ValidationError(
        '<span style="color: red;">Номер телефона должен содержать только цифры и быть не более 11 символов.</span>',
        code='invalid',
    )
class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, verbose_name='Кличка', null=True)
    species = models.ForeignKey('Species', on_delete=models.PROTECT, to_field='id',verbose_name='Разновидность')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, verbose_name='Пол')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    location = models.CharField(max_length=255, verbose_name='Место')
    phone = models.CharField(max_length=11, verbose_name='Телефон', validators=[validate_phone_number])
    lost = models.ForeignKey('Lost', on_delete= models.PROTECT,null=True, verbose_name='Статус')
    photo = models.ImageField(upload_to='images/', default=None, blank=True, null=True, verbose_name='Добавить фото')


    class Meta:
        verbose_name = 'Животные'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return self.name
class Species(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Разновидность'
        verbose_name_plural = 'Разновидность'

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

    def __str__(self):
        return self.name

class Lost(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

    def __str__(self):
        return self.name