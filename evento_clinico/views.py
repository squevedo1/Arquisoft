from django.shortcuts import render
from .logic import evento_clinico_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import EventoClinicoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from Arquisoft.auth0backend import getRole

@login_required
def eventos_clinicos_view(request):
    role = getRole(request)
    if role == "Medico":
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if id:
                evento_clinico_dto = vl.get_evento(id)
                evento_clinico = serializers.serialize('json', [evento_clinico_dto,])
                return HttpResponse(evento_clinico, 'application/json')
            else:
                eventos_clinicos_dto = vl.get_eventos_clinicos()
                eventos_clinicos = serializers.serialize('json', eventos_clinicos_dto)
                return HttpResponse(eventos_clinicos, 'application/json')

        if request.method == 'POST':
            evento_clinico_dto = vl.create_evento_clinico(json.loads(request.body))
            evento_clinico = serializers.serialize('json', [evento_clinico_dto,])
            return HttpResponse(evento_clinico, 'application/json')
    else:
        return HttpResponse("Unauthorized user")

@login_required
def evento_clinico_view(request, pk):
    role = getRole(request)
    if role == "Medico":

        if request.method == 'GET':
            evento_clinico_dto = vl.get_evento(pk)
            evento_clinico = serializers.serialize('json', [evento_clinico_dto,])
            return HttpResponse(evento_clinico, 'application/json')

        if request.method == 'PUT':
            evento_clinico_dto = vl.update_evento(pk, json.loads(request.body))
            evento_clinico = serializers.serialize('json', [evento_clinico_dto,])
            return HttpResponse(evento_clinico, 'application/json')
    else:
        return HttpResponse("Unauthorized User")

@login_required    
def evento_clinico_create(request):
    role = getRole(request)
    if role == "Medico":

        if request.method == 'POST':
            form = EventoClinicoForm(request.POST)
            if form.is_valid():
                try:
                    vl.create_evento_clinico(form)
                    messages.add_message(request, messages.SUCCESS, 'Successfully created evento medico')
                    return HttpResponseRedirect(reverse('evento_clinico_create'))
                except Exception as e:
                    print(f"Error en create_evento_clinico: {e}")
                    messages.add_message(request, messages.ERROR, 'Error al crear evento médico')
                    return render(request, 'measurementCreate.html', {'form': form})
            else:
                print(form.errors)
        else:
            form = EventoClinicoForm
    
        context = {
            'form': form
        }
    
        return render(request, 'measurementCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")


@login_required
def eventos_list(request):
    role = getRole(request)
    if role == "Medico":

        eventos = vl.get_eventos_clinicos()
        context = {
            'eventos_list': eventos
        }
        return render(request, 'measurements.html', context)
    else:
        return HttpResponse("Unauthorized User")
