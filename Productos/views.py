from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

# def crear_producto(request):
#     if request.method == 'POST':
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Producto creado correctamente.')
#             return redirect('lista_productos')
#     else:
#         form = ProductoForm()
#     return render(request, 'form.html', {'form': form, 'titulo': 'Nuevo Producto'})

@xframe_options_exempt
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Avisar al iframe que debe cerrarse:
            return HttpResponse(
                "<script>window.parent.postMessage({action: 'closeBootbox'}, '*');</script>"
            )
    else:
        form = ProductoForm()
    return render(request, 'form.html', {'form': form})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES , instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return HttpResponse(
                "<script>window.parent.postMessage({action: 'closeBootbox'}, '*');</script>"
            )
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Producto'})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return HttpResponse(
            "<script>window.parent.postMessage({action: 'closeBootbox'}, '*');</script>"
        )
    return render(request, 'confirmar_eliminacion.html', {'objeto': producto, 'tipo': 'Producto'})
