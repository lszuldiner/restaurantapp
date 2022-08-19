from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

from App_Resto.forms import ContactoFormulario, FranquiciaForm, SuscripcionForm
from App_Resto.models import Category, Consulta, Franquicia, Productos, Suscripcion

from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

from django.shortcuts import render

from App_Resto.forms import ContactoFormulario
from App_Resto.models import Consulta, Productos

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


def inicio(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miForm = SuscripcionForm(request.POST)

        if miForm.is_valid():

            data = miForm.cleaned_data

            suscripcion = Suscripcion(email=data['email'])

            suscripcion.save()

            return render(request, 'suscripto.html')

    else:

        miForm = SuscripcionForm()

    return render(request, "inicio.html", {"miForm": miForm})


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

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        formlog = AuthenticationForm(request, data=request.POST)

        if formlog.is_valid():

            data = formlog.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})

            else:

                return render(request, "inicio.html", {"mensaje": "Error, datos incorrectos"})

        return render(request, "inicio.html", {"mensaje": "Error, formulario invalido"})

    else:

        formlog = AuthenticationForm()

    return render(request, "login.html", {"formlog": formlog})


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


def platos(request):
    if request.user.is_authenticated:
        return render(request, "platos.html", context = {"categories":Category.objects.all})
    else:
        return render(request, "login.html")


def carrito(request):
    if request.user.is_authenticated:
        return render(request, "carrito.html")
    else:
        return redirect("orders:login")
        
    return render(request, "resultadoBusqueda.html")



