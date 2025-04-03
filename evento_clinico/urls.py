from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('eventos_clinicos/', views.eventos_clinicos_view, name='eventos_clinicos_view'),
    path('<int:pk>', views.evento_clinico_view, name='evento_clinico_view')
]