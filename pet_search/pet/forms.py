from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import LoginForm

from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'age', 'gender','color','location','phone','lost', 'photo']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

       
class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        
        return super(MyCustomLoginForm, self).login(*args, **kwargs)