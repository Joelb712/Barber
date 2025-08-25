from django.urls import path
from .views import *

urlpatterns=[
    path('ventas/', lista_ventas, name='lista_ventas'),
    path('ventas/nuevo/', crear_venta, name='formvent'),
]