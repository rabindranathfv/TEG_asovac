# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-26 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitraje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_temporal', models.DateTimeField(auto_now=True)),
                ('correcciones', models.TextField(blank=True, max_length=100)),
                ('resultado_del_arbitraje', models.TextField(blank=True, max_length=50)),
                ('razones_rechazo', models.TextField(blank=True, max_length=100)),
                ('observaciones', models.TextField(blank=True, max_length=100)),
                ('estatus', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=5)),
                ('cedula_pasaporte', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('linea_investigacion', models.CharField(max_length=50)),
                ('telefono_oficina', models.CharField(max_length=20)),
                ('telefono_habitacion_celular', models.CharField(max_length=20)),
                ('institucion_trabajo', models.CharField(max_length=50)),
                ('datos_institucion', models.CharField(max_length=100)),
                ('areas_interes', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, max_length=100)),
                ('clave_arbitro', models.CharField(max_length=100)),
                ('Sistema_asovac_id', models.ManyToManyField(to='main_app.Sistema_asovac')),
                ('arbitraje_id', models.ManyToManyField(blank=True, to='arbitrajes.Arbitraje')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, max_length=100)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrajes.Area')),
            ],
        ),
        migrations.AddField(
            model_name='arbitro',
            name='subarea_id',
            field=models.ManyToManyField(to='arbitrajes.Sub_area'),
        ),
        migrations.AddField(
            model_name='arbitro',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Usuario_asovac'),
        ),
    ]
