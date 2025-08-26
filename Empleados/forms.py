from django import forms
from Otros.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['usuario', 'dni', 'nombre', 'apellido', 'telefono', 'especialidad', 'activo']