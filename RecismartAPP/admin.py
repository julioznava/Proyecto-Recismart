from django.contrib import admin
from .models import *
from .forms import RegistroAvisoForm

# Register your models here.


admin.site.register(CuentaUsuario)
admin.site.register(Regiones)
admin.site.register(Comunas)
admin.site.register(RegistroAviso)



