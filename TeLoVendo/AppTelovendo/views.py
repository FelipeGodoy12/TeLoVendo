from django.shortcuts import render

from .forms import proveedorform
from .models import Provedore

# Create your views here.
def index(request):
    return render(request, 'AppTelovendo/index.html')

def contacto(request):
    return render(request, 'AppTelovendo/Contacto.html')

def estadisticas(request):
    return render(request, 'AppTelovendo/estadisticas.html')

def formulario(request):

    form = proveedorform()
    if request.method == 'POST':
        print('pasamos el post')
        form = proveedorform(request.POST)
        if form.is_valid():
            proveedor = Provedore()
            proveedor.nombre_proveedor = form.data['nombre_proveedor']
            proveedor.categoria = form.data['categoria']
            proveedor.direccion = form.data['direccion']
            proveedor.telefono_proveedor = form.data['telefono_proveedor']
            proveedor.email_proveedor = form.data['email_proveedor']
            proveedor.save()
        else:
            print('invalido')

    return render(request, 'AppTelovendo/formulario.html',{'form': form})