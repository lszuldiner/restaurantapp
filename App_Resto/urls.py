from django.contrib import admin
from django.urls import path

from App_Resto.models import Pedidos, Productos

from .views import agregar_avatar, buscar, busquedaProducto, consultas, contacto, editarPerfil, franquicias, inicio, menu, nosotros, loginView, register, reservasClientes, reservasDueno

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name="Inicio"),
    path('menu/', menu, name="Menu"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('busquedaProducto/', busquedaProducto, name="BusquedaProducto"),
    path('consultas/', contacto, name="Consultas"),
    path('buscar/', buscar, name="Buscar"),
    path('franquicias/', franquicias, name="Franquicias"),
    path('login/', loginView, name="Login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('registrar/', register, name="Registrar"),
    path("reservasClientes/", reservasClientes, name="ReservasClientes"),
    path("reservasDueno/", reservasDueno, name="ReservasDueno"),
    path('editar-perfil/', editarPerfil, name="EditarPerfil"),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
    ]