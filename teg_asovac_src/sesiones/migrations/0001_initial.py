# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-10 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arbitrajes', '0001_initial'),
    ]

    operations = [
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
                ('Sesion', models.CharField(max_length=15)),
                ('fecha_sesion', models.DateTimeField()),
                ('coordinadores', models.CharField(max_length=100)),
                ('nombre_sesion', models.CharField(max_length=50)),
                ('modalidad', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, max_length=100)),
                ('fecha_presentacion', models.DateTimeField()),
                ('arbitraje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrajes.Arbitraje')),
                ('espacio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sesiones.Espacio')),
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
    ]
