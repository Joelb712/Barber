from django import forms
from Otros.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['usuario', 'dni', 'nombre', 'apellido', 'telefono', 'especialidad', 'activo']
        widgets = {
            'usuario': forms.Select(attrs={
                'class': 'form-control'
            }),
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
            'especialidad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            }
        labels = {
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'activo': 'Activo'
            }