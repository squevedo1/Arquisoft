from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world! Django views")

def index(request):
    return render(request, 'index.html')

def healthCheck(request):
    return HttpResponse('ok')