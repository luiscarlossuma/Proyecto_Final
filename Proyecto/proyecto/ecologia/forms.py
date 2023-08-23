from django import forms
from .models import Reportes

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['fec_rep', 'asunto', 'detalles']