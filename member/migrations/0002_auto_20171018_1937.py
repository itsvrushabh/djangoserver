# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-18 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
