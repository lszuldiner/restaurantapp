from multiprocessing import context
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from App_Resto.forms import (
    AvatarFormulario, ContactoFormulario,
     FranquiciaForm, ProductosForm, ReservasForm, UserEditForm
)

from App_Resto.models import Avatar, Consulta, Franquicia, Productos, Reservas

from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

# Create your views here.
def inicio(self):
    return render(self, "inicio.html")


def menu(self):
    return render(self, "menu.html")

def consultas(self):
    return render(self, "consultas.html")

def contacto(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = ContactoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            consultas = Consulta(nombre=data['nombre'], asunto=data['asunto'], email=data['email'], mensaje=data['mensaje'])

            consultas.save()

            return render(request, 'gracias.html')

    else:

        miFormulario = ContactoFormulario()

    return render(request, "consultas.html", {"miFormulario": miFormulario})


def nosotros(self):
    return render(self, "nosotros.html")

def busquedaProducto(request):
    return render(request, "busquedaProducto.html")

def buscar(request):

    if request.GET["prd"]:

        producto=request.GET["prd"]

        productos=Productos.objects.filter(nombre__icontains=producto)
        
        return render(request, "resultadoBusqueda.html", {"productos": productos, "producto": producto})
    
    else:
        mensaje ="No se ha introducido nada"

    return render(request, "resultadoBusquedaNada.html")


def franquicias(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        Formulario = FranquiciaForm(request.POST)

        if Formulario.is_valid():

            data = Formulario.cleaned_data

            franquicias = Franquicia(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], telefono=data['telefono'], zona=data['zona'])

            franquicias.save()

            return render(request, 'graciasFranquicia.html')

    else:

        Formulario = FranquiciaForm()

    return render(request, "franquicias.html", {"Formulario": Formulario})


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('ReservasDueno')
        else:
            messages.info(request, 'Usuario Invalido')
            return redirect('Login')

    else:
        return render(request, 'login.html')
                                            #LEER MENU#
def leermenu(request):
    menu = Productos.objects.all()
    contexto= {"menu":menu}
    return render(request, 'leermenu.html', contexto)

                                            #AGREGAR MENU#


class MenuListView(ListView):
    model = Productos
    template_name = "menu-listar.html"

class menuCreateView(CreateView):
    model = Productos
    template_name = "menu-crear.html"
    fields= ('__all__')
    success_url= '/App_Resto/menu-listar'

class menuUpdateView(UpdateView):
    model = Productos
    template_name = "menu-editar.html"
    fields= ('__all__')
    success_url= '/App_Resto/'


class menuDetailView(DetailView):
    model = Productos
    template_name = "menu-detallar.html"



class menuDeleteView(DeleteView):
    model = Productos
    template_name = "menu-eliminar.html"
    success_url= '/App_Resto/menu-listar'







@login_required
def reservasDueno(request):
    db = Reservas.objects.all()
    return render(request, 'reservasDueno.html', {'db':db})



def reservasClientes(request):
    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        form = ReservasForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            reservas = Reservas(nombre=data['nombre'], email=data['email'], telefono=data['telefono'], numero_personas=data['numero_personas'], dia=data['dia'], horario=data['horario'])

            reservas.save()

            return render(request, 'graciasReservas.html')

    else:

        form = ReservasForm()

    return render(request, "reservasCliente.html", {"form": form})


def editarPerfil(request):
    
    print('method:', request.method)
    print('post:', request.POST)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password = data["password1"]

            usuario.save()

            return render(request, "inicio.html", {"mensaje": "Datos actualizados con éxito..."})

    else:

        miFormulario = UserEditForm(instance=request.user)

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario})




class ReservaUpdate(UpdateView):

    model = Reservas
    template_name = 'reservasUpdate.html'
    fields = ('__all__')
    success_url = '/App_Resto/reservasDueno'

class ReservaDelete(DeleteView):

    model = Reservas
    template_name = 'reservasDelete.html'
    success_url = '/App_Resto/reservasDueno'

class ReservaDetail(DetailView):

    model = Reservas
    template_name = 'reservasDetail.html'
    context_object_name = '/App_Resto/reservasDueno'




def agregar_avatar(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user=request.user, imagen=data['imagen'])

            avatar.save()

            return render(request, 'inicio.html', {"mensaje": "Avatar cargado"})

    else:

        miFormulario = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado'})

    else:

        form = UserCreationForm()

    return render(request, "registro.html", {"miFormulario": form})











