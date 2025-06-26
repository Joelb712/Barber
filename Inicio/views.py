from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,'index.html')