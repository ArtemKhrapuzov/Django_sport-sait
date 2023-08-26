from django import forms
from django.core.validators import RegexValidator

from .models import Muscle, Exercises, Client


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
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона необходимо вводить в формате: «+999999999». Допускается до 15 цифр.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone', 'target']

