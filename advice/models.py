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
    name = models.CharField(max_length=50)
    function = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='image/')

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    muscle = models.ManyToManyField(Muscle, related_name='muscle')

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя', validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', validators=[MinLengthValidator(4)])
    target = models.CharField(max_length=9, choices=TARGET,  verbose_name='Цель', default='other')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона необходимо вводить в формате: «+999999999». Допускается до 15 цифр.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True, verbose_name='Телефон')

    def __str__(self):
        return f"{self.first_name} {self.last_name} номер телефона: {self.phone}"
