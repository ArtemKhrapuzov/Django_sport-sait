from django.db import models
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
