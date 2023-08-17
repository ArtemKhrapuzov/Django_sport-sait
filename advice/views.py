from django.shortcuts import render, reverse
from django.http import HttpResponse


def main_menu(request):
    return render(request, 'advice/main_menu.html')


def workout(request):
    return render(request, 'advice/workout.html')

def nutrition(request):
    return render(request, 'advice/nutrition.html')

def disease(request):
    return render(request, 'advice/disease.html')