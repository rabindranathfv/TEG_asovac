# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0009_auto_20190212_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='trabajo_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajos.Trabajo'),
        ),
    ]