
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AnimalForm, RegisterForm
from .models import Animal

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': "Все животные", 'url_name': 'all_animal'},
        {'title': "Добавить объявление", 'url_name': 'add_animal'},

        ]


def all_animal(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'menu': menu,'animals':animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'animal_detail.html', {'menu': menu,'animal': animal})


class Add_animal(CreateView):
    form_class = AnimalForm
    template_name = 'add_animal.html'
    success_url = reverse_lazy('home')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить объявление'
        context['menu'] = menu
        return context

#@login_required
# def add_animal(request):
#     if request.method == 'POST':
#         form = AnimalForm(request.POST, request.FILES)
#         if form.is_valid():
#             animal = form.save(commit=False)
#             animal.owner = request.user
#             animal.save()
#     else:
#         form = AnimalForm()
#
#     return render(request, 'add_animal.html', {'menu': menu,'form': form, 'title': 'Добавить объявление'})


def home(request):
    animals = Animal.objects.all()
    context = {'menu': menu,
               'title': 'Главная',
               'animals': animals

    }
    return render(request, 'home.html', context=context)


def about(request):
    return render(request, 'about.html', {'menu': menu, 'title': 'О сайте'})


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
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['menu'] = menu
        return context
