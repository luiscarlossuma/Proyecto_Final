from django import forms
from .models import Reportes

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['fec_rep', 'asunto', 'detalles']

    #Para hacer la validacion de la forma
    def clean(self):
        cleaned_data = super().clean()
        fec_rep = cleaned_data.get('fec_rep')
        asunto = cleaned_data.get('asunto')
        detalles = cleaned_data.get('detalles')

        if not fec_rep or not asunto or not detalles:
            raise forms.ValidationError("Todos los campos deben estar completos")
        return cleaned_data