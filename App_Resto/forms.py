from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Reservas
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

from App_Resto.models import Avatar

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    asunto = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=200)

class ProductosForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=150)
    precio = forms.IntegerField()
    tipo = forms.CharField(max_length=30)

class FranquiciaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    zona = forms.CharField(max_length=50)

class ReservasForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField(max_value=1599999999)
    numero_personas= forms.IntegerField(initial=1,min_value=1,max_value=6)
    dia = forms.DateField(widget=forms.Select(choices=Reservas.dias_))
    horario = forms.CharField(widget=forms.Select(choices=Reservas.horarios_))


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']




class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)


