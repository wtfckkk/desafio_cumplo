from django import forms

from apps.indicadores.models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta

        fields = [
            'fecha_inicio',
            'fecha_fin',
            'tipo_consulta',
        ]
        labels = {
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Fin',
            'tipo_consulta': 'Tipo de Consulta',
        }
        widgets = {
            'fecha_inicio': forms.TextInput(attrs={'class':'datepicker form-control','autocomplete':'off'}),
            'fecha_fin': forms.TextInput(attrs={'class':'datepicker form-control','autocomplete':'off'}),
            'tipo_consulta': forms.Select(attrs={'class': 'form-control'}),
        }
