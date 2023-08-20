from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Muscle, Exercises

def main_menu(request):
    return render(request, 'advice/main_menu.html')


def training(request):
    muscle = Muscle.objects.all()
    return render(request, 'advice/training.html', {'muscle': muscle})

def muscle(request, muscle_id):
    muscle = Muscle.objects.get(id=muscle_id)
    exercise = Exercises.objects.filter(muscle=muscle)
    context = {
        'muscle': muscle,
        'exercise': exercise,
    }
    return render(request, 'advice/muscle.html', context=context)

def nutrition(request):
    return render(request, 'advice/nutrition.html')

def disease(request):
    return render(request, 'advice/disease.html')