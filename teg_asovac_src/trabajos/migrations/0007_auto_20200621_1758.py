# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-06-21 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0006_trabajo_se_carga_correccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='resumen',
            field=models.TextField(),
        ),
    ]
