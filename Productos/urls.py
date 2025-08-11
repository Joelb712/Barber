from django.urls import path
from .views import *

urlpatterns=[
    path('catalogo/productos/',catalogo_productos, name='catalogo_productos'),
    path('carga/formprod/',formulariop,name="formp"),
]
