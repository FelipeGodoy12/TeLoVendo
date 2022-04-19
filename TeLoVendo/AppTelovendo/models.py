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