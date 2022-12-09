from django.contrib import admin
from .models import *
from .forms import RegistroAvisoForm

# Register your models here.

class ImageAvisoAdmin(admin.TabularInline):
    model = ImageAviso
class AvisosAdmin(admin.ModelAdmin):
    form = RegistroAvisoForm
    inlines = [
        ImageAvisoAdmin
    ]


admin.site.register(CuentaUsuario)
admin.site.register(CuentaRecolector)
admin.site.register(Regiones)
admin.site.register(Comunas)
admin.site.register(RegistroAviso)



