# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 00:42
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
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('dia_asignado', models.DateTimeField()),
                ('duracion', models.CharField(max_length=50)),
                ('horario_preferido', models.CharField(max_length=50)),
                ('fecha_preferida', models.DateTimeField()),
                ('observaciones', models.TextField(max_length=100)),
                ('url_anuncio_evento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Locacion_evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.TextField(max_length=100)),
                ('descripcion', models.TextField(max_length=100)),
                ('capacidad_de_asistentes', models.IntegerField()),
                ('observaciones', models.TextField(max_length=100)),
                ('equipo_requerido', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula_o_pasaporte', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('institucion', models.CharField(max_length=50)),
                ('telefono_oficina', models.CharField(max_length=20)),
                ('telefono_habitacion_celular', models.CharField(max_length=20)),
                ('direccion_correspondencia', models.TextField(max_length=100)),
                ('es_miembro_asovac', models.BooleanField(default=False)),
                ('capitulo_asovac', models.CharField(max_length=50)),
                ('cargo_en_institucion', models.CharField(max_length=50)),
                ('url_organizador', models.CharField(max_length=100)),
                ('observaciones', models.TextField(max_length=100)),
                ('usuario_asovac', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Usuario_asovac')),
            ],
        ),
        migrations.CreateModel(
            name='Organizador_evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locacion_preferida', models.CharField(max_length=50)),
                ('evento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
                ('organizador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Organizador')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='locacion_evento_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Locacion_evento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador_id',
            field=models.ManyToManyField(through='eventos.Organizador_evento', to='eventos.Organizador'),
        ),
    ]