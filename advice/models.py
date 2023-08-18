from django.db import models
from django.urls import reverse


class Workout(models.Model):
    name = models.CharField(max_length=100)
    muscle_groups = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, blank=True)
    group = models.ForeignKey(Workout, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.name