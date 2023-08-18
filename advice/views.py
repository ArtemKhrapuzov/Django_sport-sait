from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Workout, Exercise

def main_menu(request):
    return render(request, 'advice/main_menu.html')


def workout(request):
    workout = Workout.objects.all()
    return render(request, 'advice/workout.html', {'workout': workout})

def group(request, group_id: str):
    muscle_group = get_object_or_404(Exercise, id=group_id)
    context = {
        'muscle_group': muscle_group,
        'group': group_id,
    }
    return render(request, 'advice/muscle_group.html', context=context)


def nutrition(request):
    return render(request, 'advice/nutrition.html')

def disease(request):
    return render(request, 'advice/disease.html')