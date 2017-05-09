from datetime import datetime, timedelta
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from reservaciones.forms import ReservaEmpleadoForm
from reservaciones.models import Sala, Reservacion, Insumo, InsumoSala, InsumoReservacion


class ReservacionesView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'home.html')
        else:
            return render(request, 'reservaciones/reservar.html')

class ReservacionesListView(ListView):
    model = Reservacion
    template_name = 'reservaciones/reservaciones_list.html'
    queryset = Reservacion.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            admin = True
        else:
            admin = False

        return render(request, self.template_name, context={'admin': admin, 'reserva_list': self.get_queryset().all()})

class ReservacionesDetailView(DetailView):
    model = Reservacion
    template_name = 'reservaciones/reservaciones_detail.html'

class ReservacionesCreateView(CreateView):
    model = Reservacion
    template_name = 'reservaciones/reservaciones_form.html'
    success_url = reverse_lazy('reservaciones:list')
    fields = [
        'user', 'sala', 'cantidad_personas', 'hora_inicio', 'hora_termino', 'estatus', 'fecha'
    ]

class ReservacionesUpdateView(UpdateView):
    model = Reservacion
    template_name = 'reservaciones/reservaciones_form.html'
    success_url = reverse_lazy('reservaciones:list')
    fields = [
        'user', 'sala', 'cantidad_personas', 'hora_inicio', 'hora_termino', 'estatus', 'fecha'
    ]

class ReservacionesDeleteView(DeleteView):
    model = Reservacion
    template_name = 'reservaciones/reservaciones_confirm_delete.html'
    success_url = reverse_lazy('reservaciones:list')

class ReservaEmpleadoView(FormView):
    form_class = ReservaEmpleadoForm
    success_url = 'reservaciones/salas_disponibles.html'
    template_name = 'reservaciones/reserva.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            cantidad = form.validated_data()['cantidad_personas']
            insumos = form.validated_data()['insumos']

            salas = Sala.objects.exclude(
                id__in=Reservacion.objects.all().values_list('sala_id', flat=True),
                capacidad__lte=cantidad, insumosala__insumo__in=insumos
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