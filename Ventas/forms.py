from django import forms
from Otros.models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente','empleado','total','caja','activo']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-select'}),
            'empleado': forms.Select(attrs={'class':'form-select'}),
            'total': forms.NumberInput(attrs={'class':'form-control','placeholder':'Total'}),
            'caja': forms.Select(attrs={'class':'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }