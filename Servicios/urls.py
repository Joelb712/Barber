from django.urls import path
from .views import *

urlpatterns=[
    path('servicios/', lista_servicios, name='lista_servicios'),
    path('servicios/nuevo/', crear_servicio, name='formserv'),
]