from django import forms
from .models import EventoMedico

class EventoClinicoForm(forms.ModelForm):
    class Meta:
        model = EventoMedico
        fields = [
            'historia_clinica',
            'Tipo_evento',
            'fecha_y_hora_del_evento',
            'especificaciones'
        ]
        labels = {
            'historia_clinica': 'Historia',
            'Tipo_evento': 'Tipo_evento',
            'fecha_y_hora_del_evento': 'fecha_y_hora_del_evento',
            'especificaciones': 'especificaciones'
        }