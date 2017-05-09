from django.contrib import admin

# Register your models here.
from sala_reuniones.models import Sala

class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'capacidad', 'horario_disponibilidad')

admin.site.register(Sala, SalaAdmin)