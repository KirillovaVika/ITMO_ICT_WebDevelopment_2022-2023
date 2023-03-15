# Generated by Django 4.1.4 on 2023-02-09 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211110_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='answer',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='grade',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]