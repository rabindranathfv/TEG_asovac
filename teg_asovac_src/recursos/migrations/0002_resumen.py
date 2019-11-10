# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-11-09 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_sistema_asovac_slogan'),
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resumen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_portada', models.CharField(blank=True, max_length=200, null=True)),
                ('url_patrocinadores', models.CharField(blank=True, max_length=200, null=True)),
                ('comision_organizadora', models.TextField(blank=True, null=True)),
                ('pie_pagina', models.TextField(blank=True, null=True)),
                ('sistema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Sistema_asovac')),
            ],
        ),
    ]
