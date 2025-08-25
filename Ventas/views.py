from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Venta
from .forms import VentaForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt


def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})

@xframe_options_exempt
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            # Avisar al iframe que debe cerrarse:
            return HttpResponse(
                "<script>window.parent.postMessage({action: 'closeBootbox'}, '*');</script>"
            )
    else:
        form = VentaForm()
    return render(request, 'formvent.html', {'form': form})