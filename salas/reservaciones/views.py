from datetime import datetime, timedelta
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView

from reservaciones.forms import ReservaEmpleadoForm
from reservaciones.models import Sala, Reservacion, Insumo, InsumoSala, InsumoReservacion




class ReservaEmpleadoView(FormView):
    form_class = ReservaEmpleadoForm
    success_url = 'reservaciones/salas_disponibles.html'
    template_name = 'reservaciones/reserva.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            cantidad = form.validated_data()['cantidad_personas']
            insumos = form.validated_data()['insumos']

            salas = Sala.objects.filter(capacidad__gte=cantidad, insumosala__insumo__in=insumos).exclude(
                id__in=Reservacion.objects.filter(estatus__in=(2, 3)).values_list('sala_id', flat=True)
            )

            arreglo_salas = []

            for sala in salas:
                ins = InsumoSala.objects.filter(sala=sala)
                dic = {
                    'sala': sala,
                    'insumos': ins
                }
                arreglo_salas += [dic]

            return render(request, self.success_url, context={
                'salas_disponibles': arreglo_salas,
                'cantidad_personas': cantidad,
                'insumos': insumos})


class ReservaCreateView(CreateView):
    template_name = 'reservaciones/reserva_exitosa.html'

    def post(self, request, *args, **kwargs):
        sala = request.POST.get('sala', None)
        horario_disponibilidad = request.POST.get('horario_disponibilidad', None)
        cantidad_personas = request.POST.get('cantidad_personas', None)
        insumos = request.POST.get('insumos', None)

        hora_termino = datetime.strptime(horario_disponibilidad, '%H:%M') + timedelta(hours=1)

        if sala:
            sala_instance = Sala.objects.get(id=sala)
            instance = Reservacion.objects.create(
                fecha=datetime.now(), hora_inicio=horario_disponibilidad,
                hora_termino=hora_termino.time(),
                cantidad_personas=cantidad_personas, sala=sala_instance, user=request.user,
                estatus=2
            )

            for insumo in insumos:
                insumo_instance = Insumo.objects.get(id=insumo)
                InsumoReservacion.objects.create(insumo=insumo_instance, reservacion=instance)

        return render(request, self.template_name, context={'mensaje': 'Sala reservada exitosamente!'})