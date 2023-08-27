# Generated by Django 4.2.4 on 2023-08-26 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0010_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «+999999999». Допускается до 15 цифр.', regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон'),
        ),
    ]