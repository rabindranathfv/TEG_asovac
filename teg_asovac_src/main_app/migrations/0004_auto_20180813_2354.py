# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-13 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20180812_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario_asovac',
            name='estado_arbitraje',
        ),
        migrations.AddField(
            model_name='sistema_asovac',
            name='estado_arbitraje',
            field=models.SmallIntegerField(default=0),
        ),
    ]
