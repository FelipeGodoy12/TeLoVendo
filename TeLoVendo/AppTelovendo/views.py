from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'AppTelovendo/index.html')

def contacto(request):
    return render(request, 'AppTelovendo/Contacto.html')

def estadisticas(request):
    return render(request, 'AppTelovendo/estadisticas.html')