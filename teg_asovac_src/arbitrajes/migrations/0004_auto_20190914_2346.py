# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-09-14 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbitrajes', '0003_auto_20190913_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbitro',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10),
        ),
    ]
