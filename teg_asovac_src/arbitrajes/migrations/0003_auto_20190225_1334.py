# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-25 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbitrajes', '0002_auto_20190118_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbitro',
            name='titulo',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
