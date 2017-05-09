from __future__ import unicode_literals

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.db.models.fields.related import ForeignKey

from sala_reuniones.models import Sala


ESTATUS_RESERVACION = (
    (1, 'No Disponible'),
    (2, 'Disponible'),
    (3, 'Reservada'),
    (4, 'Confirmada'),
)

class Reservacion(models.Model):
    """
    Modelo de reservacion
    """
    sala = ForeignKey(Sala, on_delete=models.PROTECT)
    user = ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha = models.DateField('Fecha de reservacion')
    hora_inicio = models.TimeField('Hora inicio')
    hora_termino = models.TimeField('Hora termino')
    cantidad_personas = models.IntegerField('Cantidad de personas')
    estatus = models.IntegerField('Estatus', help_text='indica el estatus de la sala', choices=ESTATUS_RESERVACION)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Reservacion'
        verbose_name_plural = 'Reservaciones'


class Insumo(models.Model):
    """
    Modelo de insumos
    """
    nombre = models.TextField('Nombre', max_length=30, help_text='indica el nombre del insumo')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'


class InsumoReservacion(models.Model):
    """
    Modelo que indica los insumos solicitados en la reservacion
    """
    insumo = ForeignKey(Insumo, on_delete=models.CASCADE, verbose_name='Insumo')
    reservacion = ForeignKey(Reservacion, on_delete=models.CASCADE, verbose_name='Reservacion')

    class Meta:
        verbose_name = 'Insumo de Reservacion'
        verbose_name_plural = 'Insumo de Reservaciones'


class InsumoSala(models.Model):
    """
    Modelo que indica los insumos que se pueden alquilar en la sala
    """
    insumo = ForeignKey(Insumo, on_delete=models.CASCADE, verbose_name='Insumo')
    sala = ForeignKey(Sala, on_delete=models.CASCADE, verbose_name='Sala')

    def __str__(self):
        return self.insumo.nombre

    class Meta:
        verbose_name = 'Insumo de Sala'
        verbose_name_plural = 'Insumo de Salas'