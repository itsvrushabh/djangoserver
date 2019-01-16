# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-12 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0001_initial'),
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_reviews', to='trip.Trip'),
        ),
    ]
