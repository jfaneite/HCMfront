from django.contrib import admin

# Register your models here.
from reservaciones.models import Reservacion, Insumo, InsumoSala, InsumoReservacion


class InsumoSalaAdmin(admin.ModelAdmin):
	list_display = ('insumo', 'sala')

class InsumoReservacionAdmin(admin.ModelAdmin):
	list_display = ('insumo', 'reservacion')

class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sala', 'fecha', 'hora_inicio', 'hora_termino', 'cantidad_personas', 'estatus')

class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)



admin.site.register(InsumoSala, InsumoSalaAdmin)
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(InsumoReservacion, InsumoReservacionAdmin)