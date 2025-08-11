from django.shortcuts import render
import random

# Create your views here.
def catalogo_productos(request):
    productos_data = [
        {"nombre": "Pomada Fijadora", "imagen":  "https://picsum.photos/200?random=1"},
        {"nombre": "Cera Mate", "imagen":  "https://picsum.photos/200?random=2"},
        {"nombre": "Shampoo Anticaspa", "imagen":  "https://picsum.photos/200?random=3"},
        {"nombre": "Acondicionador Hidratante", "imagen":  "https://picsum.photos/200?random=4"},
        {"nombre": "Tónico Capilar", "imagen":  "https://picsum.photos/200?random=5"},
        {"nombre": "Aceite para Barba", "imagen":  "https://picsum.photos/200?random=6"},
        {"nombre": "Gel para Cabello", "imagen":  "https://picsum.photos/200?random=7"},
        {"nombre": "Spray Fijador", "imagen":  "https://picsum.photos/200?random=8"},
        {"nombre": "Mousse Voluminizador", "imagen":  "https://picsum.photos/200?random=9"},
        {"nombre": "Shampoo Barba", "imagen":  "https://picsum.photos/200?random=10"},
        {"nombre": "Bálsamo para Barba", "imagen":  "https://picsum.photos/200?random=11"},
        {"nombre": "Pomada con Brillo", "imagen":  "https://picsum.photos/200?random=12"},
        {"nombre": "Crema Moldeadora", "imagen":  "https://picsum.photos/200?random=13"},
        {"nombre": "Espuma para Rulos", "imagen":  "https://picsum.photos/200?random=14"},
        {"nombre": "Cepillo Redondo", "imagen":  "https://picsum.photos/200?random=15"},
        {"nombre": "Peine de Dientes Anchos", "imagen":  "https://picsum.photos/200?random=16"},
        {"nombre": "Cera Natural", "imagen":  "https://picsum.photos/200?random=17"},
        {"nombre": "Pomada Strong", "imagen":  "https://picsum.photos/200?random=18"},
        {"nombre": "Gel Extreme", "imagen":  "https://picsum.photos/200?random=19"},
        {"nombre": "Spray Antifrizz", "imagen":  "https://picsum.photos/200?random=35"},
    ]

    productos = []
    for p in productos_data:
        productos.append({
            "nombre": p["nombre"],
            "precio": random.choice([2500, 3200, 3900, 4500, 5000, 5800, 6200]),  # todos terminan en .00
            "imagen": p["imagen"] + "?auto=format&fit=crop&w=640&q=80",
            "ventas": random.randint(0, 100),
        })

    mas_vendidos = sorted(productos, key=lambda x: -x["ventas"])[:5]
    menos_vendidos = sorted(productos, key=lambda x: x["ventas"])[:5]

    return render(request, "productos.html", {
        "productos": productos,
        "mas_vendidos": mas_vendidos,
        "menos_vendidos": menos_vendidos,
    })

def formulariop(request):
    return render(request, 'formprod.html')