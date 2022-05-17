from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView


from .forms import proveedorform, UserRegistrerForm, ComentarioForm
from .models import Comentarios, Provedore

# Create your views here.
def index(request):
    return render(request, 'AppTelovendo/index.html')

def estadisticas(request):
    return render(request, 'AppTelovendo/estadisticas.html')

class Formulario(FormView):
    template_name = 'AppTelovendo/formulario.html'
    form_class = proveedorform
    success_url = '/proveedores'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

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