from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,'index.html')

def dash(request):
    return render(request,'dash.html')