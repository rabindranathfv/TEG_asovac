# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-08 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0003_auto_20180908_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateField(),
        ),
    ]
