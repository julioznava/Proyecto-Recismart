from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # TESTING
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


# TESTING
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Ingrese un correo valido...', required=True)

    class Meta:
        model = get_user_model()
        # fields = ['first_name', 'last_name, 'username', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super(UserRegistrationForm).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'user_permissions', 'date_joined', 'last_login']


