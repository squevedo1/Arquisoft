from django.db import models
from pacientes.models import Paciente
from django.core.exceptions import ValidationError

class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    aclaraciones = models.TextField(blank=True, null=True)

    def clean(self):
        # Validación para asegurar que el paciente exista
        if not Paciente.objects.filter(id=self.paciente.id).exists():
            raise ValidationError('Debe existir un paciente asociado para crear una Historia Clínica.')

    def __str__(self):
        return f"Historia Clínica de {self.paciente.nombre}"
