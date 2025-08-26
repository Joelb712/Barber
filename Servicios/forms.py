from django import forms
from Otros.models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'duracion_minutos', 'activo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }