from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, './templates/index.html')

def healthCheck(request):
    return HttpResponse('ok')