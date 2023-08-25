from django import forms
from .models import *

NUMBER_OF_WORKOUT = (
    ('Не тренируюсь', 'Не тренируюсь'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('Больше 5', 'Больше 5'),
)

SEX = (
    ('male', 'Мужской пол'),
    ('female', 'Женский пол')
)


class Calorie(forms.Form):
    sex = forms.ChoiceField(choices=SEX, label='Пол')
    weight = forms.IntegerField(min_value=35, max_value=250, label='Вес')
    height = forms.IntegerField(min_value=100, max_value=230, label='Рост')
    age = forms.IntegerField(min_value=14, max_value=80, label='Возраст')
    number_of_workouts = forms.ChoiceField(choices=NUMBER_OF_WORKOUT, label='Колличество тренировок в неделю')


class AddClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone']
