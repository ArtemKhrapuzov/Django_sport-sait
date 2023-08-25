from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


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
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    #target = models.TextField(max_length=500, verbose_name='Цель')
    phone = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Телефон')

    def __str__(self):
        return f"{self.first_name} {self.last_name} номер телефона: {self.phone}"
