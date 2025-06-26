from django.urls import path
from django.contrib.auth import views as auth_views
from Usuarios import views

urlpatterns = [
    path('registrarse/',views.Registrarse, name ='Registrarse'),
    path('sesion/', views.InicioSesion, name='InicioSesion'),
    path('cerrar/', views.CerrarSesion, name='CerrarSesion'),
]
