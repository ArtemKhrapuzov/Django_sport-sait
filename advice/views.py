from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import *
from .models import *


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


def consultation(request):
    if request.method == 'POST':
        form = AddClient(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('main_menu')
            except:
                raise form.add_error(None, 'Ошибка добавления данных')
    else:
        form = AddClient()
    return render(request, 'advice/consultation.html', {'form': form})


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
                BMR = round((10 * weight) + (6.25 * height) - (5 * age) + 5, 0)
            else:
                BMR = round((10 * weight) + (6.25 * height) - (5 * age) - 161, 0)
            if number_of_workouts == 'Не тренируюсь':
                result = round(BMR * 1.2, 0)
            elif number_of_workouts == '1' or number_of_workouts == '2':
                result = round(BMR * 1.375, 0)
            elif number_of_workouts == '3' or number_of_workouts == '4' or number_of_workouts == '5':
                result = round(BMR * 1.55, 0)
            elif number_of_workouts == 'Больше 5':
                result = round(BMR * 1.9, 0)
            result_loss = round(result * 0.8, 1)
            result_up = round(result * 1.2, 1)
            context = {
                'calorie': calorie,
                'weight': weight,
                'height': height,
                'sex': sex,
                'age': age,
                'number_of_workouts': number_of_workouts,
                'BMR': BMR,
                'result': result,
                'result_loss': result_loss,
                'result_up': result_up,
            }
            return render(request, 'advice/weight_loss.html', context)
    else:
        calorie = Calorie()
    return render(request, 'advice/weight_loss.html', {'calorie': calorie})
