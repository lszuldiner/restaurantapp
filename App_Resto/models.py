
from datetime import datetime
from tabnanny import verbose
from django.db import models

# Create your models here.
class Clientes(models.Model):
    
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre} - {self.direccion} - {self.email}'

    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Productos(models.Model):
    
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre} - {self.precio}'

    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'

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

class Suscripcion(models.Model):

    email = models.EmailField()


    def __str__(self) -> str:
        return f'{self.email}'



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

class Category(models.Model):
    category_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category_gif = models.ImageField(upload_to="Fotosprodu")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f'{self.category_title}'
