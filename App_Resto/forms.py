from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Reservas

from App_Resto.models import Avatar

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    asunto = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=200)


class FranquiciaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    zona = forms.CharField(max_length=50)

class ReservasForm(forms.Form):
    class Meta:
        model = Reservas
        fields = '__all__'


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