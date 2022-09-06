from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from App_Resto.forms import (
    AvatarFormulario, UserEditForm
)
from App_Resto.models import Avatar, Consulta, Franquicia, Productos, Reservas
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import update_session_auth_hash
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


# Create your views here.
def inicio(request):

    try:
        avatar= Avatar.objects.get(user=request.user.id)
        return render(request, "inicio.html",{"url":avatar.imagen.url})
    except:
        return render(request, "inicio.html")

def nosotros(request):
    try:    
        avatar= Avatar.objects.get(user=request.user.id)
        return render(request, "nosotros.html",{"url":avatar.imagen.url})
    except:
        return render(request, "nosotros.html",)

def about(request):
    try:
        avatar= Avatar.objects.get(user=request.user.id)
        return render(request, "about.html",{"url":avatar.imagen.url})
    except:
        return render(request, "about.html")

def busquedaProducto(request):
    try:
        avatar= Avatar.objects.get(user=request.user.id)
        return render(request, "busquedaProducto.html",{"url":avatar.imagen.url})
    except:
        return render(request, "busquedaProducto.html")

def buscar(request):
    
    if request.GET["prd"]:

        producto=request.GET["prd"]

        productos=Productos.objects.filter(nombre__icontains=producto)
        
        return render(request, "resultadoBusqueda.html", {"productos": productos, "producto": producto})
    
    else:
        mensaje ="No se ha introducido nada"

    return render(request, "resultadoBusquedaNada.html")


##########################################LOGIN###################################
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)

                return render(request,"inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:

                return render(request,"inicio.html", {"mensaje": "Error, datos incorrectos"})
        else:

                return render(request,"inicio.html", {"mensaje": "Error, Formulario Erroneo"})
    else:

        form = AuthenticationForm()
        return render(request,"login.html", {'form':form} )

##########################################REGISTRO###################################

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado exitosamente'})

    else:

        form = UserCreationForm()

    return render(request, "registro.html", {"miFormulario": form})

######################################EDITARUSUARIO#############################################
@login_required
def editarPerfil(request):
    
    print('method:', request.method)
    print('post:', request.POST)

    usuario = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():

            data = form.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            usuario.save()

            return render(request, "inicio.html", {"mensaje": "Datos actualizados con éxito..."})

    else:

        form = UserEditForm(instance=request.user)

    return render(request, "editarPerfil.html", {"form": form})

#####################################################CAMBIARPASSWORD#####################################
@login_required
def cambiar_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, "inicio.html", {"mensaje":"Tu Contraseña fue modificada con éxito!"})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'cambiar_password.html', {'form': form})

###################################################EDITARAVATAR###############################
@login_required
def agregar_avatar(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user=request.user, imagen=data['imagen'])

            avatar.save()

            return render(request, 'inicio.html', {"mensaje": "Avatar agregado correctamente."})

    else:

        miFormulario = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})

######################################CAMBIARAVATAR#################################

@login_required
def cambiar_avatar(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user=request.user, imagen=data['imagen'])

            avatar.save()

            return render(request, 'inicio.html', {"mensaje": "Avatar agregado correctamente."})

    else:

        miFormulario = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})

######################################MENU#############################################
class menuUserListView(ListView):
    model = Productos
    template_name = "menu-usuario.html"

class menuListView(LoginRequiredMixin, ListView):
    model = Productos
    template_name = "menu-listar.html"

class menuCreateView(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = "menu-crear.html"
    fields= ('__all__')
    success_url= '/App_Resto/menu-listar'

class menuUpdateView(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = "menu-editar.html"
    fields= ('__all__')
    success_url= '/App_Resto/menu-listar'

class menuDetailView(DetailView):
    model = Productos
    template_name = "menu-detallar.html"

class menuDeleteView(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = "menu-eliminar.html"
    success_url= '/App_Resto/menu-listar'

###############################################CONSULTAS#######################################

class consultaListView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = "consulta-listar.html"

class consultaCreateView(LoginRequiredMixin, CreateView):
    model = Consulta
    template_name = "consulta-crear.html"
    fields= ('__all__')
    success_url= '/App_Resto/'

class consultaUpdateView(LoginRequiredMixin, UpdateView):
    model = Consulta
    template_name = "consulta-editar.html"
    fields= ('__all__')
    success_url= '/App_Resto/consulta-listar'

class consultaDetailView(LoginRequiredMixin, DetailView):
    model = Consulta
    template_name = "consulta-detallar.html"

class consultaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = "consulta-eliminar.html"
    success_url= '/App_Resto/consulta-listar'

################################FRANQUICIAS#########################

class franquiciaListView(LoginRequiredMixin, ListView):
    model = Franquicia
    template_name = "franquicia-listar.html"

class franquiciaCreateView(LoginRequiredMixin, CreateView):
    model = Franquicia
    template_name = "franquicia-crear.html"
    fields= ('__all__')
    success_url= '/App_Resto/'
    extra_context = {"mensaje" : "Solicitud de franquicia enviada exitosamente."}

class franquiciaUpdateView(LoginRequiredMixin, UpdateView):
    model = Franquicia
    template_name = "franquicia-editar.html"
    fields= ('__all__')
    success_url= '/App_Resto/franquicia-listar'

class franquiciaDetailView(LoginRequiredMixin, DetailView):
    model = Franquicia
    template_name = "franquicia-detallar.html"

class franquiciaDeleteView(LoginRequiredMixin, DeleteView):
    model = Franquicia
    template_name = "menu-eliminar.html"
    success_url= '/App_Resto/franquicia-listar'

###############################################Intento de Mail#######################################

# @login_required
# def reservasDueno(request):
#     db = Reservas.objects.all()
#     return render(request, 'reservasDueno.html', {'db':db})



# def reservasClientes(request):
#     print('method:', request.method)
#     print('post:', request.POST)

#     if request.method == 'POST':

#         form = ReservasForm(request.POST)

#         if form.is_valid():

#             data = form.cleaned_data

#             reservas = Reservas(
#                 nombre=data['nombre'],
#                 email=data['email'],
#                 telefono=data['telefono'], 
#                 numero_personas=data['numero_personas'],
#                 dia=data['dia'],
#                 horario=data['horario']
#                 )

#             reservas.save()
            
#             name= request.POST['nombre']
#             subject= f"Reservación de {request.POST['nombre']}, para el día  {request.POST['dia']}"
#             email= request.POST['email']
#             message= f"Reservación de {request.POST['nombre']}, para el día  {request.POST['dia']}, a las {request.POST['horario']} HS"
#             telefono= request.POST['telefono']
#             numero_personas= request.POST['numero_personas']
#             dia= request.POST['dia']
#             horario= request.POST['horario']

#             template= render_to_string('email_template.html',{
#                 'name': name,
#                 'subject': subject,
#                 'email': email,
#                 'message': message,
#                 'telefono': telefono,
#                 'numero_personas': numero_personas,
#                 'dia': dia,
#                 'horario': horario
#                 })
#             correo = EmailMessage(
#                 subject,
#                 template,
#                 settings.EMAIL_HOST_USER,
#                 ['soykaza@gmail.com']
#             )

#             correo.fail_silently = False
#             correo.send()
#             messages.success(request, "Se envió un correo.")
#             return redirect('inicio')

#     else:

#         form = ReservasForm()

#     return render(request, "reservasCliente.html", {"form": form})

# def EmailEnviar(request):
#     if request.method == "POST":
#         name= request.POST['nombre']
#         subject= f"Reservación de {request.POST['nombre']}, para el día  {request.POST['dia']}"
#         email= request.POST['email']
#         message= f"Reservación de {request.POST['nombre']}, para el día  {request.POST['dia']}, a las {request.POST['horario']} HS"
#         telefono= request.POST['telefono']
#         numero_personas= request.POST['numero_personas']
#         dia= request.POST['dia']
#         horario= request.POST['horario']




#         template= render_to_string('email_template.html',{
#             'name': name,
#             'subject': subject,
#             'email': email,
#             'message': message,
#             'telefono': telefono,
#             'numero_personas': numero_personas,
#             'dia': dia,
#             'horario': horario
#             })
#         correo = EmailMessage(
#             subject,
#             template,
#             settings.EMAIL_HOST_USER,
#             ['soykaza@gmail.com']
#         )

#         correo.fail_silently = False
#         correo.send()
#         messages.success(request, "Se envió un correo.")
#         return redirect('inicio')
#####################################################RESERVAS#############################################
class reservaListView(LoginRequiredMixin, ListView):
    model = Reservas
    template_name = "reserva-listar.html"

class reservaCreateView(LoginRequiredMixin, CreateView):
    model = Reservas
    template_name = "reserva-crear.html"
    fields= ('__all__')
    success_url= '/App_Resto/'

class reservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservas
    template_name = "reserva-editar.html"
    fields= ('__all__')
    success_url= '/App_Resto/reserva-listar'

class reservaDetailView(LoginRequiredMixin, DetailView):
    model = Reservas
    template_name = "reserva-detallar.html"

class reservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservas
    template_name = "reserva-eliminar.html"
    success_url= '/App_Resto/reserva-listar'


















