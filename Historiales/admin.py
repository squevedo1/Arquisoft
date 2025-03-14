from django.contrib import admin
from .models import HistoriaClinica, Paciente, EventoMedico

admin.site.register(Paciente)
admin.site.register(HistoriaClinica)
admin.site.register(EventoMedico)
