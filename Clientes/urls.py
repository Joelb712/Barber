from django.urls import path
from .views import *

urlpatterns=[
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', crear_cliente, name='formcli'),
]