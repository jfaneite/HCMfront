from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from sala_reuniones.models import Sala


class SalasListView(ListView):
    model = Sala
    template_name = 'salas/salas_list.html'
    queryset = Sala.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            admin = True
        else:
            admin = False

        return render(request, self.template_name, context={'admin': admin, 'sala_list': self.get_queryset().all()})

class SalasDetailView(DetailView):
    model = Sala
    template_name = 'salas/sala_detail.html'

class SalasCreateView(CreateView):
    model = Sala
    template_name = 'salas/sala_form.html'
    success_url = reverse_lazy('salas:list')
    fields = [
        'nombre', 'ubicacion', 'capacidad', 'hora_apertura', 'hora_cierre'
    ]

class SalasUpdateView(UpdateView):
    model = Sala
    template_name = 'salas/sala_form.html'
    success_url = reverse_lazy('salas:list')
    fields = [
        'nombre', 'ubicacion', 'capacidad', 'hora_apertura', 'hora_cierre'
    ]

class SalasDeleteView(DeleteView):
    model = Sala
    template_name = 'salas/sala_confirm_delete.html'
    success_url = reverse_lazy('salas:list')