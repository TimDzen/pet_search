from django.contrib.auth import logout

from django.contrib.auth.forms import  AuthenticationForm

from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AnimalForm, RegisterForm, MyCustomLoginForm
from .models import Animal

menu = [{'title': "На Главную", 'url_name': 'home'},
        {'title': "Добавить объявление", 'url_name': 'add_animal'},
        {'title': "Все животные", 'url_name': 'all_animal'},
        {'title': 'Связаться с нами', 'url_name': 'about'},

        ]


def all_animal(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'menu': menu,'animals':animals, 'title': 'Все объявления'})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'animal_detail.html', {'menu': menu,'animal': animal})



class Add_animal(CreateView):
    form_class = AnimalForm
    template_name = 'add_animal.html'
    success_url = reverse_lazy('all_animal')


    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить объявление'
        context['menu'] = menu
        return context

def home(request):
    animals = Animal.objects.all()
    context = {'menu': menu,
               'title': 'Главная',
               'animals': animals,
               'user': request.user,


    }
    return render(request, 'home.html', context=context)


def about(request):
    return render(request, 'about.html', {'menu': menu, 'title': 'Контакты'})


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['menu'] = menu
        return context

class LoginUser(LoginView):
    form_class = MyCustomLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['menu'] = menu
        return context

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


