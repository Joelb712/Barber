from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Servicio
from .forms import ServicioForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt


def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

@xframe_options_exempt
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            # Avisar al iframe que debe cerrarse:
            return HttpResponse(
                "<script>window.parent.postMessage({action: 'closeBootbox'}, '*');</script>"
            )
    else:
        form = ServicioForm()
    return render(request, 'formserv.html', {'form': form})