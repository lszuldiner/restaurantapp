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
    nombre = forms.CharField(max_length=150)
    precio = forms.IntegerField()

class FranquiciaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    zona = forms.CharField(max_length=50)

class ReservasForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField(initial= 1122334455, min_value=10000000,max_value=1600000000)
    numero_personas= forms.IntegerField(
        initial=1,min_value=1,max_value=6,help_text="Minimo 1, Máximo 6 personas por mesa")
    dia = forms.DateField(help_text="Ingrese Fecha (Dia,Mes,Año)", initial=datetime.today)
    horario = forms.TimeField(help_text="Ingrese hora (Hora:Minutos)")


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden..")
        return password2



class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)