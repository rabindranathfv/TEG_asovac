# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sesiones', '0002_auto_20180703_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sesion',
            old_name='arbitraje_id',
            new_name='arbitraje',
        ),
        migrations.RenameField(
            model_name='sesion',
            old_name='espacio_id',
            new_name='espacio',
        ),
    ]
