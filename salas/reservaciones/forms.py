from django import forms
from reservaciones.models import Insumo


class ReservaEmpleadoForm(forms.Form):
    cantidad_personas = forms.IntegerField()
    insumos = forms.ModelMultipleChoiceField(queryset=Insumo.objects.all())


    def validated_data(self):
        return self.data