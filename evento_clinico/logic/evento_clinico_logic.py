from ..models import EventoMedico

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
    evento = EventoMedico(historia_clinica=var["historia_clinica"], Tipo_evento=var["Tipo_evento"],
                          fecha_y_hora_del_evento=var["fecha_y_hora_del_evento"], especificaciones=var["especificaciones"])
    evento.save()
    return evento