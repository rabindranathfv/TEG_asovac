# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-04-28 15:45
from __future__ import unicode_literals

import django.core.validators
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
                ('nombre', models.CharField(max_length=150)),
                ('categoria', models.CharField(choices=[('P', 'Presencial'), ('V', 'Virtual')], max_length=50)),
                ('descripcion', models.TextField(max_length=150)),
                ('tipo', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('dia_asignado', models.DateField()),
                ('duracion', models.CharField(max_length=50)),
                ('horario_preferido', models.CharField(max_length=50)),
                ('fecha_preferida', models.DateField()),
                ('observaciones', models.TextField(blank=True, max_length=400)),
                ('url_anuncio_evento', models.CharField(max_length=200, validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Locacion_evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
                ('capacidad_de_asistentes', models.SmallIntegerField(default=0)),
                ('observaciones', models.TextField(blank=True, max_length=400)),
                ('equipo_requerido', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('genero', models.SmallIntegerField(choices=[(0, 'Masculino'), (1, 'Femenino')], default=0)),
                ('cedula_o_pasaporte', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('institucion', models.CharField(max_length=50)),
                ('telefono_oficina', models.CharField(max_length=20)),
                ('telefono_habitacion_celular', models.CharField(max_length=20)),
                ('direccion_correspondencia', models.TextField(max_length=100)),
                ('es_miembro_asovac', models.BooleanField(choices=[(False, 'No es miembro de AsoVAC'), (True, 'Es miembro de AsoVAC')], default=False)),
                ('capitulo_asovac', models.CharField(max_length=50)),
                ('cargo_en_institucion', models.CharField(max_length=50)),
                ('url_organizador', models.CharField(max_length=200)),
                ('observaciones', models.TextField(blank=True, max_length=400)),
                ('usuario_asovac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuarios_asovac_organizadores', to='main_app.Usuario_asovac')),
            ],
        ),
        migrations.CreateModel(
            name='Organizador_evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locacion_preferida', models.CharField(max_length=50)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Eventos', to='eventos.Evento')),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Organizadores', to='eventos.Organizador')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='locacion_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locacion_eventos', to='eventos.Locacion_evento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador_id',
            field=models.ManyToManyField(related_name='Organizador_eventos', through='eventos.Organizador_evento', to='eventos.Organizador'),
        ),
    ]
