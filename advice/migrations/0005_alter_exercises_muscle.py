# Generated by Django 4.2.4 on 2023-08-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0004_remove_exercises_muscle_exercises_muscle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='muscle',
            field=models.ManyToManyField(related_name='muscle', to='advice.muscle'),
        ),
    ]
