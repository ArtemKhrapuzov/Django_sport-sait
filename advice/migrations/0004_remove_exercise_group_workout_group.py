# Generated by Django 4.2.4 on 2023-08-18 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0003_rename_description_workout_muscle_groups_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='group',
        ),
        migrations.AddField(
            model_name='workout',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='advice.workout'),
        ),
    ]
