# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-09 02:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sala_reuniones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(help_text='indica el nombre del insumo', max_length=30, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='InsumoReservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Insumo')),
            ],
        ),
        migrations.CreateModel(
            name='InsumoSala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Insumo')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala_reuniones.Sala')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de reservacion')),
                ('hora_inicio', models.TimeField(verbose_name='Hora inicio')),
                ('hora_termino', models.TimeField(verbose_name='Hora termino')),
                ('cantidad_personas', models.IntegerField(verbose_name='Cantidad de personas')),
                ('estatus', models.IntegerField(choices=[(1, 'No Disponible'), (2, 'Disponible'), (3, 'Reservada'), (4, 'Confirmada')], help_text='indica el estatus de la sala', verbose_name='Estatus')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sala_reuniones.Sala')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='insumoreservacion',
            name='reservacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Reservacion'),
        ),
    ]
