# Generated by Django 4.2.4 on 2023-08-26 01:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0007_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='target',
            field=models.CharField(choices=[('nutrition', 'Питание'), ('training', 'Тренировки'), ('full', 'Полное ведение'), ('other', 'Другое')], default='other', max_length=9, verbose_name='Цель'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон'),
        ),
    ]