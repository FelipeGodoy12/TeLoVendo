from django import forms

from .models import Provedore
    
    
class proveedorform(forms.ModelForm):
    class Meta:
        model = Provedore
        fields = ("nombre_proveedor", "categoria", "direccion", "telefono_proveedor", "email_proveedor",)

    

