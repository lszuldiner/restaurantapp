from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone


# Create your models here.

class Productos(models.Model):
    
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} - ${self.precio}'
    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Pedidos(models.Model):
    
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.numero} - {self.fecha} - {self.entregado}'

    class Meta():
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class Consulta(models.Model):

    nombre = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.asunto} - {self.email} - {self.mensaje}'

    class Meta():
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'



class Franquicia(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    zona = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.apellido} - {self.email} - {self.telefono}- {self.zona}'

    class Meta():
        verbose_name = 'Franquicia'
        verbose_name_plural = 'Franquicias'



class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    numero_personas= models.IntegerField()
    dia = models.DateField()
    horario = models.TimeField()

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f'{self.nombre}'


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

