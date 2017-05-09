from __future__ import unicode_literals
from django.db import models


class Sala(models.Model):
    """
    Modelo de sala
    """
    nombre = models.TextField('Nombre', max_length=30, help_text='indica el nombre de la sala')
    ubicacion = models.TextField('Ubicacion', max_length=30, help_text='indica la ubicacion de la sala')
    capacidad = models.IntegerField('Capacidad', help_text='indica  la capacidad en numero de personas de la sala')
    horario_disponibilidad = models.TimeField('Horario de Disponibilidad', help_text='indica la hora disponible')

    def __str__(self):
        return self.nombre

    def get_horario_disponibilidad(self):
        return self.horario_disponibilidad.strptime('%H:%M:%S')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
