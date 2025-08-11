from django.urls import path
from .views import *

urlpatterns=[
    path('',Inicio,name='Inicio'),
    path('dash',dash,name='dash'),
    path('catalogo/servicios/',catalogo_servicios, name='catalogo_servicios'),
    path('carga/formserv/',formularios,name="forms"),
    path('contacto/',contacto,name='contacto'),
    path('tienda/',tienda,name='tienda'),
]
