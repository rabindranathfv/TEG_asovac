# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-04-25 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autores', '0001_initial'),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinadores_sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinador', models.BooleanField(default=False)),
                ('co_coordinador', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autores.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ocupacion', models.DateTimeField()),
                ('tipo_espacio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Espacio_fisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('capacidad', models.IntegerField()),
                ('ubicacion', models.TextField(blank=True, max_length=100)),
                ('video_beam', models.BooleanField(default=False)),
                ('portatil', models.BooleanField(default=False)),
                ('turno', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Espacio_virtual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_virtual', models.CharField(max_length=100)),
                ('capacidad_url', models.IntegerField()),
                ('turno', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sesion', models.CharField(max_length=25)),
                ('lugar', models.CharField(max_length=50)),
                ('fecha_sesion', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('observaciones', models.TextField(blank=True, max_length=100)),
                ('capacidad', models.IntegerField()),
                ('video_beam', models.BooleanField(default=False)),
                ('portatil', models.BooleanField(default=False)),
                ('coordinadores', models.ManyToManyField(through='sesiones.Coordinadores_sesion', to='autores.Autor')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Sistema_asovac')),
            ],
        ),
        migrations.AddField(
            model_name='espacio',
            name='espacio_fisico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sesiones.Espacio_fisico'),
        ),
        migrations.AddField(
            model_name='espacio',
            name='espacio_virtual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sesiones.Espacio_virtual'),
        ),
        migrations.AddField(
            model_name='coordinadores_sesion',
            name='sesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesiones.Sesion'),
        ),
    ]
