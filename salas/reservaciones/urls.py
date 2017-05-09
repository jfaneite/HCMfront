from django.conf.urls import url

from reservaciones.views import ReservaEmpleadoView, ReservaCreateView

urlpatterns = [
    url(r'^reserva$', ReservaEmpleadoView.as_view(), name='reserva'),
    url(r'^reserva/crear$', ReservaCreateView.as_view(), name='crearReserva'),

]