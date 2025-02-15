from django import forms
from .models import Producto,UserPerfil,Anime,Marca,Serie,Venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

# CREA EL FORMULARIO PARA PRODUCTOS

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class UpdateProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','anime','marca','serie','descripcion','tp_producto','precio','foto']

# FROM PARA EL REGISTRO USUARIOS

class UserForm(UserCreationForm):
    username=forms.CharField(min_length=5,max_length=50)
    nombre=forms.CharField(min_length=3, max_length=50)
    apellido=forms.CharField(min_length=4, max_length=50)

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserPerfilForm(forms.ModelForm):

    class Meta:
        model=UserPerfil
        fields=['fono','city','direccion']

class UpdateUserPerfilForm(forms.ModelForm):

    class Meta:
        model=UserPerfil
        fields=['fono','city','direccion']

# FORM PARA REGISTRO ANIME
class AnimeForm(forms.ModelForm):

    class Meta:
        model = Anime
        fields = ['nombre']

# FORM PARA REGISTRO MARCA
class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['nombre']

# FORM PARA REGISTRO SERIE
class SerieForm(forms.ModelForm):

    class Meta:
        model = Serie
        fields = ['nombre']

# FORM PARA ESTADO VENTAS
class EstadoVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['estado']