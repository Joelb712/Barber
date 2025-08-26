from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})

@xframe_options_exempt
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            # Avisar al iframe que debe cerrarse:
            return HttpResponse(
                "<script>window.parent.postMessage({action: 'closeBootbox'}, '*');</script>"
            )
    else:
        form = EmpleadoForm()
    return render(request, 'formemp.html', {'form': form})