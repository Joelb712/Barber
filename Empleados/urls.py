from django.urls import path
from .views import *

urlpatterns=[
    path('empleados/', lista_empleados, name='lista_empleados'),
    path('empleados/nuevo/', crear_empleado, name='formemp'),
]