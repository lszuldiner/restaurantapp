from django.contrib import admin
from django.urls import path

from App_Resto.models import Pedidos, Productos

from .views import (login_request, menuListView, agregar_avatar,buscar, busquedaProducto, editarPerfil, inicio, menuCreateView,
 cambiar_password ,menuDeleteView, menuDetailView, menuUpdateView, nosotros, register, consultaListView , consultaCreateView,
 consultaDetailView,consultaDeleteView, menuUserListView, franquiciaListView, franquiciaCreateView, franquiciaUpdateView,
 franquiciaDetailView, franquiciaDeleteView, reservaListView, reservaCreateView, reservaUpdateView, reservaDetailView, reservaDeleteView
)

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls, name="SuperUserView"),
    path('', inicio, name="Inicio"),
    path('menu-listar/', menuListView.as_view(), name="MenuListar"),
    path('menu-usuario/', menuUserListView.as_view(), name="MenuUsuario"),
    path('menu-crear/', menuCreateView.as_view(), name="MenuCrear"),
    path('menu-editar/<int:pk>', menuUpdateView.as_view(), name="MenuEditar"),
    path('menu-detallar/<int:pk>', menuDetailView.as_view(), name="MenuDetallar"),
    path('menu-eliminar/<int:pk>', menuDeleteView.as_view(), name="MenuEliminar"),
    path('consulta-listar/', consultaListView.as_view(), name="ConsultaListar"),
    path('consulta-crear/', consultaCreateView.as_view(), name="ConsultaCrear"),
    path('consulta-gracias/', consultaCreateView.as_view(), name="ConsultaGracias"),
    path('consulta-detallar/<int:pk>', consultaDetailView.as_view(), name="ConsultaDetallar"),
    path('consulta-eliminar/<int:pk>', consultaDeleteView.as_view(), name="ConsultaEliminar"),

    path('franquicia-listar/', franquiciaListView.as_view(), name="FranquiciaListar"),
    path('franquicia-crear/', franquiciaCreateView.as_view(), name="FranquiciaCrear"),
    path('franquicia-editar/<int:pk>', franquiciaUpdateView.as_view(), name="FranquiciaEditar"),
    path('franquicia-detallar/<int:pk>', franquiciaDetailView.as_view(), name="FranquiciaDetallar"),
    path('franquicia-eliminar/<int:pk>', franquiciaDeleteView.as_view(), name="FranquiciaEliminar"),

    path('reserva-listar/', reservaListView.as_view(), name="ReservaListar"),
    path('reserva-crear/', reservaCreateView.as_view(), name="ReservaCrear"),
    path('reserva-editar/<int:pk>', reservaUpdateView.as_view(), name="ReservaEditar"),
    path('reserva-detallar/<int:pk>', reservaDetailView.as_view(), name="ReservaDetallar"),
    path('reserva-eliminar/<int:pk>', reservaDeleteView.as_view(), name="ReservaEliminar"),

    path('nosotros/', nosotros, name="Nosotros"),
    path('busquedaProducto/', busquedaProducto, name="BusquedaProducto"),
    path('buscar/', buscar, name="Buscar"),

    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('registrar/', register, name="Registrar"),
    path('editar-perfil/', editarPerfil, name="EditarPerfil"),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
    path('cambiar-password/', cambiar_password, name="CambiarPassword"),

    ]