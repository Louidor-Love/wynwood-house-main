# Generated by Django 5.0.6 on 2024-05-30 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='arrival_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='property',
            name='departure_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='property',
            name='guest_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
