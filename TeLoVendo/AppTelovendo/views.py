from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import proveedorform, UserRegistrerForm, ComentarioForm
from .models import Comentarios, Provedore

# Create your views here.
def index(request):
    return render(request, 'AppTelovendo/index.html')

def estadisticas(request):
    return render(request, 'AppTelovendo/estadisticas.html')

def formulario(request):

    form = proveedorform()

    if request.method == 'POST':
        form = proveedorform(request.POST)
        if form.is_valid():
            proveedor = Provedore()
            proveedor.nombre_proveedor = form.data['nombre_proveedor']
            proveedor.categoria = form.data['categoria']
            proveedor.direccion = form.data['direccion']
            proveedor.telefono_proveedor = form.data['telefono_proveedor']
            proveedor.email_proveedor = form.data['email_proveedor']
            proveedor.save()
            messages.success(request, f'El proveedor {proveedor.nombre_proveedor} a sido Registrado Correctamente')
            return redirect('proveedores')
        else:
            print('invalido')

    return render(request, 'AppTelovendo/formulario.html',{'form': form})


def registrar(request):
    if request.method == 'POST':
        form = UserRegistrerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El Usuario {username} a sido Registrado Correctamente')
            return redirect('login')
    else:
        form = UserRegistrerForm()

    context = {'form':form}

    return render(request, 'AppTelovendo/registrarse.html', context)


def proveedores(request):

    proveedores = Provedore.objects.all()
    
    return render(request, 'AppTelovendo/proveedores.html',{'proveedores':proveedores})

@login_required
def ingresado(request):
    return render(request, 'AppTelovendo/ingresado.html')

def crearcomentario(request):

    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(data=request.POST)
        comentario = form.save(commit=False)
        comentario.save()
        return redirect('listarcomentarios')

    else:
        return render(request, 'AppTelovendo/contacto.html', {'form':form})

def listarcomentarios(request):
    
    
    comentario = Comentarios.objects.all()


    return render(request, 'AppTelovendo/listarcomentarios.html', {'comentario':comentario})

def editarcomentarios(request, id):
    comentario = Comentarios.objects.get(pk=id)

    form = ComentarioForm(instance=comentario)
    if request.method == 'POST':
        form = ComentarioForm(data=request.POST, instance=comentario)
        form.save()
        return redirect('listarcomentarios')

    else:
        return render(request, 'AppTelovendo/editarcomentarios.html', {'form':form})



def eliminarcomentario(request, id):
    comentario = Comentarios.objects.get(pk=id)
    comentario.delete()
    return redirect('listarcomentarios')