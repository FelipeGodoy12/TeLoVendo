from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index, name='index'),
    path('Contacto',views.contacto, name='Contacto'),
    path('estadisticas',views.estadisticas, name='estadisticas'),
    path('formulario',views.formulario, name='formulario'),

]
