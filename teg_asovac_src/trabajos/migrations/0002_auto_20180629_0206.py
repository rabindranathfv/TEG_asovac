# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='documento_inscrito',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='observaciones',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='resumen',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='url_trabajo',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='version',
            field=models.CharField(default='', max_length=20),
        ),
    ]