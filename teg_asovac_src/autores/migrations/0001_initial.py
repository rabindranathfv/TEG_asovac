# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-19 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
        ('trabajos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_temporal', models.DateTimeField(auto_now=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=1)),
                ('cedula_pasaporte', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('telefono_oficina', models.CharField(max_length=20)),
                ('telefono_habitacion_celular', models.CharField(max_length=20)),
                ('constancia_estudio', models.CharField(blank=True, max_length=255)),
                ('direccion_envio_correspondencia', models.TextField(blank=True, max_length=100)),
                ('es_miembro_asovac', models.BooleanField(default=False)),
                ('capitulo_perteneciente', models.CharField(blank=True, max_length=20)),
                ('nivel_intruccion', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, max_length=255)),
                ('Sistema_asovac_id', models.ManyToManyField(to='main_app.Sistema_asovac')),
            ],
        ),
        migrations.CreateModel(
            name='Autores_trabajos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_autor_principal', models.BooleanField(default=False)),
                ('es_ponente', models.BooleanField(default=False)),
                ('es_coautor', models.BooleanField(default=False)),
                ('monto_total', models.FloatField()),
                ('pagado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autores.Autor')),
                ('trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajos.Trabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Datos_pagador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('pasaporte_rif', models.CharField(blank=True, max_length=20)),
                ('telefono_oficina', models.CharField(blank=True, max_length=20)),
                ('telefono_habitacion_celular', models.CharField(max_length=20)),
                ('direccion_fiscal', models.TextField(max_length=100)),
                ('Sistema_asovac_id', models.ManyToManyField(to='main_app.Sistema_asovac')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_subtotal', models.FloatField()),
                ('fecha_emision', models.DateTimeField()),
                ('iva', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pagador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorias_pago', models.CharField(max_length=20)),
                ('autor_trabajo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autores.Autores_trabajos')),
                ('datos_pagador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='autores.Datos_pagador')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pago', models.CharField(max_length=50)),
                ('numero_cuenta_origen', models.CharField(max_length=50)),
                ('banco_origen', models.CharField(max_length=50)),
                ('numero_transferencia', models.CharField(blank=True, max_length=50)),
                ('numero_cheque', models.CharField(blank=True, max_length=50)),
                ('fecha_pago', models.DateTimeField()),
                ('observaciones', models.TextField(blank=True, max_length=100)),
                ('comprobante_pago', models.FileField(upload_to='comprobantes_de_pago/')),
            ],
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('facultad', models.CharField(max_length=100)),
                ('escuela', models.CharField(max_length=100)),
                ('instituto_investigacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='pagador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autores.Pagador'),
        ),
        migrations.AddField(
            model_name='factura',
            name='pago',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='autores.Pago'),
        ),
        migrations.AddField(
            model_name='autor',
            name='universidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autores.Universidad'),
        ),
        migrations.AddField(
            model_name='autor',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Usuario_asovac'),
        ),
    ]
