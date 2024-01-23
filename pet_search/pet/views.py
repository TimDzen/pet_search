from django.shortcuts import render

from .models import Animal


def all_animal(request):
    animals = Animal.objects.all()
    return render(request, 'pet/all_animals.html', {'animals':animals })

def animal_detail(request):
    animal = Animal.objects.get(pk = animal_id)
    return render(request, 'pet/animal_detail.html', {'animal': animal})