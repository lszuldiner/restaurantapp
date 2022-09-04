from django.contrib import admin
from django.urls import path

from App_Resto.models import Pedidos, Productos

from .views import MenuListView, ReservaDelete, ReservaDetail, ReservaUpdate, agregar_avatar, buscar, busquedaProducto, consultas, contacto, editarPerfil, franquicias, inicio, leermenu, menu, menuCreateView, menuDeleteView, menuDetailView, menuUpdateView, nosotros, loginView, register, reservasClientes, reservasDueno

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('menu-listar/', MenuListView.as_view(), name="MenuListar"),
    path('menu-crear/', menuCreateView.as_view(), name="MenuCrear"),
    path('menu-editar/<int:pk>', menuUpdateView.as_view(), name="MenuEditar"),
    path('menu-detallar/<int:pk>', menuDetailView.as_view(), name="MenuDetallar"),
    path('menu-eliminar/<int:pk>', menuDeleteView.as_view(), name="MenuEliminar"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('busquedaProducto/', busquedaProducto, name="BusquedaProducto"),
    path('consultas/', contacto, name="Consultas"),
    path('buscar/', buscar, name="Buscar"),
    path('franquicias/', franquicias, name="Franquicias"),
    path('login/', loginView, name="Login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('registrar/', register, name="Registrar"),
    path("reservasClientes/", reservasClientes, name="ReservasClientes"),
    path('editar-perfil/', editarPerfil, name="EditarPerfil"),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
    path("reservasDueno/", reservasDueno, name="ReservasDueno"),
    path('actualizarReservas/<int:pk>', ReservaUpdate.as_view(), name="ActualizarReserva"),
    path('eliminarReservas/<int:pk>', ReservaDelete.as_view(), name="EliminarReserva"),
    path('detallesReservas/<int:pk>', ReservaDetail.as_view(), name="DetailReserva"),
    ]