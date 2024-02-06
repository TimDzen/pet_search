from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'age', 'gender','color','location','phone','lost', 'photo']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль')
    password2 = forms.CharField(label="Повтор пароля")
    class Meta:
        model = User
        fields = ['username','email', 'password', 'password2']