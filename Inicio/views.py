from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,'index.html')

def dash(request):
    return render(request,'dash.html')

# def catalogo_productos(request):
#     return render(request, 'productos.html')

def contacto(request):
    return render(request,'contacto.html')

def tienda(request):
    return render(request,'tienda.html')

def formularios(request):
    return render(request, 'formserv.html')

def catalogo_servicios(request):
    return render(request, 'servicios.html')


