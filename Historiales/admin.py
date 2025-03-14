from django.contrib import admin
from .models import HistoriaClinica, Paciente

admin.site.register(Paciente)
admin.site.register(HistoriaClinica)