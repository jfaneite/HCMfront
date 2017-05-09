from django.conf.urls import url

from sala_reuniones.views import SalasListView, SalasDetailView, SalasCreateView,\
    SalasUpdateView, SalasDeleteView

urlpatterns = [
    url(r'^$', SalasListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', SalasDetailView.as_view(), name='detail'),
    url(r'^nuevo$', SalasCreateView.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', SalasUpdateView.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', SalasDeleteView.as_view(), name='delete'),
]