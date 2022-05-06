from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    mail = models.EmailField(verbose_name="Ingrese Correo del Cliente")
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Provedore(models.Model):
    nombre_proveedor = models.CharField(max_length=60)
    categoria = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    telefono_proveedor = models.IntegerField(verbose_name='Ingrese Telefono del proveedor')
    email_proveedor = models.EmailField(verbose_name="Ingrese Correo del Proveedor")

    def __str__(self):
        return self.nombre_proveedor


class Vendedor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    mail = models.EmailField()
    telefono = models.IntegerField()
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Comentarios(models.Model):
    nombre = models.CharField(max_length=45)
    email = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return self.nombre