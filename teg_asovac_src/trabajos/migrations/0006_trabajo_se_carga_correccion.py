# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-09-14 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0005_auto_20190914_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='se_carga_correccion',
            field=models.BooleanField(default=False),
        ),
    ]