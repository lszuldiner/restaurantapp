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
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} - ${self.precio}'
    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'



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
    horarios_=(
        ("20:00","8:00PM"),
        ("21:00","9:00PM"),
        ("22:00","10:00PM"),
        ("23:00","11:00PM"),
        ("24:00","12:00PM"),
    )
    dias_=(
        ("lunes","Lunes"),
        ("martes","Martes"),
        ("miercoles","Miercoles"),
        ("jueves","Jueves"),
        ("viernes","Viernes"),
        ("sabado","Sabado"),
        ("domingo","Domingo")
    )

    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    numero_personas= models.IntegerField()
    dia = models.CharField(choices=dias_,max_length=9)
    horario = models.CharField(max_length=7, choices=horarios_)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f'{self.nombre} - {self.numero_personas} - {self.dia} - {self.horario}'



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.imagen}'
    