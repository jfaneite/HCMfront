from django.conf.urls import url

from reservaciones.views import ReservacionesListView, ReservacionesDetailView, ReservacionesCreateView,\
    ReservacionesUpdateView, ReservacionesDeleteView, ReservacionesView, ReservaEmpleadoView, ReservaCreateView

urlpatterns = [
    url(r'^lista/$', ReservacionesListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ReservacionesDetailView.as_view(), name='detail'),
    url(r'^nuevo$', ReservacionesCreateView.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ReservacionesUpdateView.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ReservacionesDeleteView.as_view(), name='delete'),

    url(r'^$', ReservacionesView.as_view(), name='home'),
    url(r'^reserva$', ReservaEmpleadoView.as_view(), name='reserva'),
    url(r'^reserva/crear$', ReservaCreateView.as_view(), name='crearReserva'),

]