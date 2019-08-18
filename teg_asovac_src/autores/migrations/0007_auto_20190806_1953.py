# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-08-06 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0006_autores_trabajos_esperando_modificacion_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autores_trabajos',
            name='numero_postulacion',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='postulacion_numero',
        ),
        migrations.AddField(
            model_name='factura',
            name='status',
            field=models.CharField(default='Pendiente', max_length=15),
        ),
    ]
