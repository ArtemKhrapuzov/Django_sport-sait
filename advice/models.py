from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

TARGET = (
    ('nutrition', 'Питание'),
    ('training', 'Тренировки'),
    ('full', 'Полное ведение'),
    ('other', 'Другое'),
)


class Muscle(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    function = models.CharField(max_length=200, blank=True, verbose_name='Функция')
    image = models.ImageField(null=True, blank=True, upload_to='image/', verbose_name='Картинка')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Мышечная группа'
        verbose_name_plural = 'Мышечные группы'

class Exercises(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')
    muscle = models.ManyToManyField(Muscle, related_name='muscle', verbose_name='Мышечная группа')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'



class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя', validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', validators=[MinLengthValidator(4)])
    target = models.CharField(max_length=9, choices=TARGET,  verbose_name='Цель', default='other')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона необходимо вводить в формате: «+999999999». Допускается до 15 цифр.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True, verbose_name='Телефон')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')

    def __str__(self):
        return f"{self.first_name} {self.last_name} номер телефона: {self.phone}"
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
