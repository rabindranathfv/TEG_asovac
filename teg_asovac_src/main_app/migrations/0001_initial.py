# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-12 22:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arbitrajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sistema_asovac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=255)),
                ('fecha_inicio_arbitraje', models.DateField()),
                ('fecha_fin_arbitraje', models.DateField()),
                ('estado_arbitraje', models.SmallIntegerField(default=0)),
                ('clave_maestra_coordinador_area', models.CharField(blank=True, max_length=100)),
                ('clave_maestra_arbitro_area', models.CharField(blank=True, max_length=100)),
                ('clave_maestra_coordinador_general', models.CharField(blank=True, max_length=100)),
                ('clave_maestra_arbitro_subarea', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_asovac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('Sistema_asovac_id', models.ManyToManyField(blank=True, to='main_app.Sistema_asovac')),
                ('rol', models.ManyToManyField(blank=True, to='main_app.Rol')),
                ('subarea_id', models.ManyToManyField(blank=True, to='arbitrajes.Sub_area')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
