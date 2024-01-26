from django.shortcuts import render

from .forms import AnimalForm
from .models import Animal


def all_animal(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'animals':animals })

def animal_detail(request):
    animal = Animal.objects.get(pk = 'animal_id')
    return render(request, 'animal_detail.html', {'animal': animal})

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AnimalForm()

    return render(request, 'add_animal.html', {'form': form})


def home(request):
    animals = Animal.objects.all()
    return render(request, 'home.html', {'animals': animals})