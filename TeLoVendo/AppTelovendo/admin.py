from django.contrib import admin
from . import models

# Register your models here.

class ProvedoreAdmin(admin.ModelAdmin):
    list_display = ('nombre_proveedor','direccion',)

admin.site.register(models.Provedore, ProvedoreAdmin)



admin.site.register(models.Cliente)
admin.site.register(models.Vendedor)
admin.site.register(models.Comentarios)
admin.site.register(models.Categoria)
admin.site.register(models.Subcategoria)