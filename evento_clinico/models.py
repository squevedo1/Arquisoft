from django.db import models
from historia_clinica.models import HistoriaClinica
from django.core.exceptions import ValidationError

class EventoMedico(models.Model):
    EVENTO_CHOICES = [
        ('Examen Medico', 'Examen Medico'),
        ('Consulta', 'Consulta'),
        ('Preescripcion', 'Preescripcion'),
        ('Cirugia', 'Cirugia'),
    ]

    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, related_name='eventos_medicos')
    Tipo_evento = models.CharField(max_length=50, choices=EVENTO_CHOICES)
    fecha_y_hora_del_evento = models.DateTimeField()
    especificaciones = models.TextField(blank=True, null=True)

    def clean(self):
        if not HistoriaClinica.objects.filter(id=self.historia_clinica.id).exists():
            raise ValidationError('Debe existir una Historia Clínica asociada para crear un Evento Médico.')

    def __str__(self):
        return f"{self.Tipo_evento} - {self.fecha_y_hora_del_evento}"
