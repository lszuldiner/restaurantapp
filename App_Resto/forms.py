from django import forms
from django.contrib.auth.models import User

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    asunto = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=200)

class SuscripcionForm(forms.Form):
    email = forms.EmailField()

class FranquiciaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    zona = forms.CharField(max_length=50)
    mensaje = forms.CharField(max_length=200)
