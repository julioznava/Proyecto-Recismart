from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.forms import cl_init_js_callbacks


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




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_permissions', 'date_joined', 'last_login']
