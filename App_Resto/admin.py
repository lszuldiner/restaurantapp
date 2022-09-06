from django.contrib import admin

from App_Resto.forms import ContactoFormulario, FranquiciaForm

from App_Resto.models import Avatar, Consulta, Productos, Reservas, Franquicia

from App_Resto.forms import ContactoFormulario


# Register your models here.
admin.site.register(Productos)
admin.site.register(Consulta)
admin.site.register(Franquicia)
admin.site.register(Reservas)
admin.site.register(Avatar)

