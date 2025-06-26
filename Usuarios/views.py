from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# def Registrarse(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             try:    
#                 usuario = User.objects.create_user(username= request.POST['username'],password= request.POST['password1'])
#                 usuario.save()
#                 login(request,usuario)
#                 return redirect('Inicio')
#             except:
#                 return render(request, ('Registrarse.html'), {'form' : UserCreationForm ,'error':' usuario ya existe'})
#         else:
#             return render(request, ('Registrarse.html'), {'form' : UserCreationForm ,'error':'Contraseña no coinciden'})
#     return render(request, ('Registrarse.html'), {'form' : UserCreationForm})

# def Registrarse(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             usuario = form.save()  # Crea y guarda el usuario
#             login(request, usuario)  # Loguea automáticamente
#             return redirect('Inicio')
#         else:
#             # Si hay errores, se renderiza la plantilla con el formulario con errores
#             return render(request, 'Registrarse.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'Registrarse.html', {'form': form})

def Registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()

    # Agregar clases CSS a los widgets
    form.fields['username'].widget.attrs.update({
        'class': 'form-input pl-14 py-3 w-full rounded-md text-black',
        'placeholder': 'Nombre de usuario',
        'autocomplete': 'username',
        'autofocus': True,
    })
    form.fields['password1'].widget.attrs.update({
        'class': 'form-input pl-14 py-3 w-full rounded-md text-black',
        'placeholder': 'Contraseña',
        'autocomplete': 'new-password',
    })
    form.fields['password2'].widget.attrs.update({
        'class': 'form-input pl-14 py-3 w-full rounded-md text-black',
        'placeholder': 'Repetir contraseña',
        'autocomplete': 'new-password',
    })

    if request.method == 'POST' and form.is_valid():
        usuario = form.save()
        login(request, usuario)
        return redirect('Inicio')

    return render(request, 'Registrarse.html', {'form': form})

# def InicioSesion(request):
#     if request.method == 'GET':
#         return render(request,('login.html'),{'form': AuthenticationForm})
#     else:
#         usuario = authenticate(request,username=request.POST['username'],password=request.POST['password'])
#         if usuario is None:
#             return render(request,('login.html'),{'form': AuthenticationForm}) 
#         else:
#             login(request,usuario)
#             return redirect('Inicio')


# def InicioSesion(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             usuario = form.get_user()
#             login(request, usuario)
#             return redirect('Inicio')
#     else:
#         form = AuthenticationForm()
#     # Agregar atributos manualmente en la vista
#     form.fields['username'].widget.attrs.update({
#         'class': 'form-input pl-14 py-3 w-full rounded-md text-black',
#         'placeholder': 'Email o usuario',
#         'autocomplete': 'username',
#         'autofocus': 'autofocus'
#     })
#     form.fields['password'].widget.attrs.update({
#         'class': 'form-input pl-14 py-3 w-full rounded-md text-black',
#         'placeholder': 'Contraseña',
#         'autocomplete': 'current-password'
#     })
#     return render(request, 'login.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm

def InicioSesion(request):
    form = AuthenticationForm(request, data=request.POST or None)

    form.fields['username'].widget.attrs.update({
        'class': 'form-input pl-14 py-3 w-full rounded-md text-black',
        'placeholder': 'Email o usuario',
        'autocomplete': 'username',
        'autofocus': 'autofocus'
    })

    form.fields['password'].widget.attrs.update({
        'class': 'form-input pl-14 py-3 w-full rounded-md text-black',
        'placeholder': 'Contraseña',
        'autocomplete': 'current-password'
    })

    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('Inicio')

    return render(request, 'login.html', {'form': form})

def CerrarSesion(request):
    logout(request)
    return redirect('Inicio')