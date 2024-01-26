from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import AnimalForm
from .models import Animal


def all_animal(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'animals':animals })

def animal_detail(request):
    animal = Animal.objects.get(pk = 'animal_id')
    return render(request, 'animal_detail.html', {'animal': animal})

@login_required
def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.owner = request.user
            animal.save()

    else:
        form = AnimalForm()

    return render(request, 'add_animal.html', {'form': form})


def home(request):
    animals = Animal.objects.all()
    return render(request, 'home.html', {'animals': animals})