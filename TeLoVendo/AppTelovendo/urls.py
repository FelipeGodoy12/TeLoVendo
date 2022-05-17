from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index, name='index'),
    path('estadisticas',views.estadisticas, name='estadisticas'),
    path('formulario',views.Formulario.as_view(), name='formulario'),
    path('registrarse',views.registrar, name='registrase'),
    path('ingresado',views.ingresado, name='ingresado'),
    path('proveedores',views.proveedores, name='proveedores'),
    path('contacto',views.crearcomentario, name='Contacto'),
    path('listarcomentarios',views.listarcomentarios, name='listarcomentarios'),
    path('editarcomentarios/<int:id>',views.editarcomentarios, name='editarcomentarios'),
    path('eliminarcomentarios/<int:id>',views.eliminarcomentario, name='eliminarcomentarios'),
    
]
