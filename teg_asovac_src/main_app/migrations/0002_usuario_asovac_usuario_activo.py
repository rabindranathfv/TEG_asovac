# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_asovac',
            name='usuario_activo',
            field=models.BooleanField(default=False),
        ),
    ]
