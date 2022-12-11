from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CuentaUsuarioForm(forms.ModelForm):

    class Meta:
        model = CuentaUsuario
        fields = '__all__'

class CuentaRecolectorForm(forms.ModelForm):

    class Meta:
        model = CuentaRecolector
        fields = '__all__'

class RegistroAvisoForm(forms.ModelForm):

    class Meta:
        model = RegistroAviso
        fields = '__all__'



class RegistroForm(UserCreationForm):
    username = forms.CharField(required=True, label= 'Crear una cuenta de usuario')
    email = forms.EmailField(required=True, label='Ingrese el mail de validacion.')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Ingrese una contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repita la contraseña')
    is_active = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_active']





# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'user_permissions', 'date_joined', 'last_login']


