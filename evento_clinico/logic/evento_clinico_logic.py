import datetime
from historia_clinica.models import HistoriaClinica
from ..models import EventoMedico
from django.core.exceptions import ObjectDoesNotExist

def get_eventos_clinicos():
    eventos = EventoMedico.objects.all()
    return eventos

def get_evento(var_pk):
    evento = EventoMedico.objects.get(pk=var_pk)
    return evento

def update_evento_clinico(evento_pk, evento_var):
    evento = get_evento(evento_pk)
    evento.especificaciones = evento_var["especificaciones"]
    evento.save()
    return evento

def create_evento_clinico(var):
    try:
        historia_clinical = HistoriaClinica.objects.get(pk=var["historia_clinica"])
    except ObjectDoesNotExist:
        raise ValueError(f"No se encontró una historia clínica con el ID {var['historia_clinica']}")
    evento = EventoMedico(historia_clinica=historia_clinical, Tipo_evento=var["Tipo_evento"],
                          fecha_y_hora_del_evento=datetime.strptime(var["fecha_y_hora_del_evento"]), 
                          especificaciones=var["especificaciones"])
    evento.save()
    return evento