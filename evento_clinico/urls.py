from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('eventos_clinicos/', views.eventos_clinicos_view, name='eventos_clinicos_view'),
    path('<int:pk>', views.evento_clinico_view, name='evento_clinico_view'),
    path('eventomedicocreate/', csrf_exempt(views.evento_clinico_create), name='evento_clinico_create')
]