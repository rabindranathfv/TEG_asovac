# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_organizador_sistema_asovac_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='locacion_evento_id',
            new_name='locacion_evento',
        ),
    ]
