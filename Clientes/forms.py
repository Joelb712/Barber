from django import forms
from Otros.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellido', 'telefono', 'email', 'notas', 'activo']
        widgets = {
            'dni': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese DNI'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }),
            'notas': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas adicionales',
                'rows': 3
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'dni': 'DNI / Documento',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'email': 'Email',
            'notas': 'Notas',
            'activo': 'Activo'
        }