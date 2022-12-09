from django.shortcuts import render
from .models import *
from.forms import *
from django.db.models import Q


#SITIO

def home(request):
    return render(request, './sitio/home.html')

def login(request):
    return render(request, './registration/login.html')


def test(request):
    return render(request, './navbar2.html')


def tiporegistro(request):
    return render(request, './sitio/tiporegistro.html')



#CLIENTES

def registro(request):
    data = {
        'form': CuentaUsuarioForm()
    }
    if request.method == 'POST':
        formulario = CuentaUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "SE HA REGISTRADO EXITOSAMENTE."
        else:
            data['form'] = formulario
    return render(request, './clientes/registro.html', data)


# ADMINISTRADOR
def panel(request):
    busqueda_usuario = request.GET.get("busqueda_usuario")
    busqueda_recolector = request.GET.get("busqueda_recolector")
    busqueda_aviso = request.GET.get("busqueda_aviso")

    listarusuario = CuentaUsuario.objects.all()
    listarrecolector = CuentaRecolector.objects.all()
    listaraviso = RegistroAviso.objects.all()

    if busqueda_usuario:
        listarusuario = CuentaUsuario.objects.filter(
            Q(Rut__icontains=busqueda_usuario) |
            Q(Nombre__icontains=busqueda_usuario) |
            Q(Apellido__icontains=busqueda_usuario) |
            Q(Correo_electronico__icontains=busqueda_usuario)
        ).distinct()

    if busqueda_recolector:
        listarrecolector = CuentaRecolector.objects.filter(
            Q(Rut_Empresa__icontains=busqueda_recolector) |
            Q(Nombre__icontains=busqueda_recolector) |
            Q(Apellido__icontains=busqueda_recolector) |
            Q(Correo_electronico__icontains=busqueda_recolector) |
            Q(Nombre_de_empresa__icontains=busqueda_recolector)
        ).distinct()

    if busqueda_aviso:
        listaraviso = RegistroAviso.objects.filter(
            Q(Titulo_de_publicacion__icontains=busqueda_aviso) |
            Q(Descripcion__icontains=busqueda_aviso)
        ).distinct()


    data = {
        'listarusuario': listarusuario,
        'listarrecolector': listarrecolector,
        'listaraviso': listaraviso,
    }
    return render(request, './administrador/panel.html', data)




#RECOLECTORES

def registrorecolector(request):
    data = {
        'form': CuentaRecolectorForm()
    }
    if request.method == 'POST':
        formulario = CuentaRecolectorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "SE HA REGISTRADO EXITOSAMENTE."
        else:
            data['form'] = formulario
    return render(request, './clientes/registro.html', data)





#PUBLICACIONES

def registroaviso(request):
    data = {
        'form': RegistroAvisoForm()
    }
    if request.method == 'POST':
        formulario = RegistroAvisoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "SE HA REGISTRADO EXITOSAMENTE."
        else:
            data['form'] = formulario
    return render(request, './publicaciones/registro.html', data)


