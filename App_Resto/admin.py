from django.contrib import admin

from App_Resto.forms import ContactoFormulario, FranquiciaForm

from App_Resto.models import Consulta, Productos, Pedidos, Reservas, Franquicia

from App_Resto.forms import ContactoFormulario

from App_Resto.models import Consulta, Productos, Pedidos


# Register your models here.
admin.site.register(Productos)
admin.site.register(Pedidos)
admin.site.register(Consulta)
admin.site.register(Franquicia)
admin.site.register(Reservas)

