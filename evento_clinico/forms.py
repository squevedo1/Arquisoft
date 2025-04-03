from django import forms
from .models import EventoMedico

class EventoClinicoForm(forms.ModelForm):
    class Meta:
        model = EventoMedico
        fields = '__all__'