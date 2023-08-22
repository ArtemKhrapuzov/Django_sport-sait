from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse

from .forms import Calorie
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


def weight_loss(request):
    if request.method == 'POST':
        calorie = Calorie(request.POST)
        if calorie.is_valid():
            sex = calorie.cleaned_data['sex']
            weight = calorie.cleaned_data['weight']
            height = calorie.cleaned_data['height']
            age = calorie.cleaned_data['age']
            number_of_workouts = calorie.cleaned_data['number_of_workouts']
            if sex == 'male':
                BMR = round(88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age), 2)
            else:
                BMR = round(447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age), 2)
            if number_of_workouts == 'Не тренируюсь':
                result = round(BMR * 1.2 * 0.9, 2)
            elif number_of_workouts == '1' or number_of_workouts == '2':
                result = round(BMR * 1.375 * 0.9, 2)
            elif number_of_workouts == '3' or number_of_workouts == '4' or number_of_workouts == '5':
                result = round(BMR * 1.55 * 0.9, 2)
            elif number_of_workouts == 'Больше 5':
                result = round(BMR * 1.9 * 0.9, 2)
            context = {
                'calorie': calorie,
                'weight': weight,
                'height': height,
                'sex': sex,
                'age': age,
                'number_of_workouts': number_of_workouts,
                'BMR': BMR,
                'result': result,
            }
            return render(request, 'advice/weight_loss.html', context)
    else:
        calorie = Calorie()
    return render(request, 'advice/weight_loss.html', {'calorie': calorie})


def weight_up(request):
    if request.method == 'POST':
        calorie = Calorie(request.POST)
        if calorie.is_valid():
            sex = calorie.cleaned_data['sex']
            weight = calorie.cleaned_data['weight']
            height = calorie.cleaned_data['height']
            age = calorie.cleaned_data['age']
            number_of_workouts = calorie.cleaned_data['number_of_workouts']
            if sex == 'male':
                BMR = round(88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age), 2)
            else:
                BMR = round(447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age), 2)
            if number_of_workouts == 'Не тренируюсь':
                result = round(BMR * 1.2 * 1.1, 2)
            elif number_of_workouts == '1' or number_of_workouts == '2':
                result = round(BMR * 1.375 * 1.1, 2)
            elif number_of_workouts == '3' or number_of_workouts == '4' or number_of_workouts == '5':
                result = round(BMR * 1.55 * 1.1, 2)
            elif number_of_workouts == 'Больше 5':
                result = round(BMR * 1.9 * 1.1, 2)
            context = {
                'calorie': calorie,
                'weight': weight,
                'height': height,
                'sex': sex,
                'age': age,
                'number_of_workouts': number_of_workouts,
                'BMR': BMR,
                'result': result,
            }
            return render(request, 'advice/weight_up.html', context)
    else:
        calorie = Calorie()
    return render(request, 'advice/weight_up.html', {'calorie': calorie})