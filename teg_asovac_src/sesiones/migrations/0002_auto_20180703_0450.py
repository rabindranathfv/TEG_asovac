# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sesiones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espacio',
            old_name='espacio_fisico_id',
            new_name='espacio_fisico',
        ),
        migrations.RenameField(
            model_name='espacio',
            old_name='espacio_virtual_id',
            new_name='espacio_virtual',
        ),
    ]
