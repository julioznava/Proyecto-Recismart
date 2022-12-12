from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from.forms import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login




#SITIO
def home(request):
    return render(request, './sitio/home.html')

def login(request):
    return render(request, './registration/login.html')


def test(request):
    return render(request, './testing/test.html')


def maspublicaciones(request):
    busqueda_aviso = request.GET.get("busqueda_aviso")
    listaraviso = RegistroAviso.objects.all()

    if busqueda_aviso:
        listaraviso = RegistroAviso.objects.filter(
            Q(Titulo_de_publicacion__icontains=busqueda_aviso) |
            Q(Descripcion__icontains=busqueda_aviso) |
            Q(Comuna__icontains=busqueda_aviso)
        ).distinct()

    data = {
        'listaraviso': listaraviso,

    }

    return render(request, './sitio/maspublicaciones.html', data)


def panelayuda(request):
    return render(request, './sitio/ayuda.html')
#CLIENTES

def registro(request):
    data = {
        'form': CuentaUsuarioCreationForm()
    }
    if request.method == 'POST':
        formulario = CuentaUsuarioCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            dj_login(request, user)
            messages.success(request, 'Te has registrado exitosamente.')
            return redirect(to="login")

        data['form'] = formulario
    return render(request, './clientes/registro.html', data)


def modificarusuario(request, id):
    modificar_user = get_object_or_404(CuentaUsuario, id=id)

    data = {
        'form':CuentaUsuarioCreationForm(instance=modificar_user)
    }
    if request.method == 'POST':
        formulario = CuentaUsuarioCreationForm(data=request.POST, instance=modificar_user)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'EL USUARIO SE HA MODIFICADO EXITOSAMENTE.'

        return redirect(to="panel")
        data["form"] = formulario

    return render(request, './clientes/modificar.html', data)


# ADMINISTRADOR
def panel(request):
    busqueda_usuario = request.GET.get("busqueda_usuario")
    busqueda_aviso = request.GET.get("busqueda_aviso")

    listarusuario = CuentaUsuario.objects.all()
    listaraviso = RegistroAviso.objects.all()

    if busqueda_usuario:
        listarusuario = CuentaUsuario.objects.filter(
            Q(Perfil_usuario__icontains=busqueda_usuario) |
            Q(Rut__icontains=busqueda_usuario) |
            # Q(Nombre__icontains=busqueda_usuario) |
            # Q(Apellido__icontains=busqueda_usuario) |
            Q(Correo__icontains=busqueda_usuario)
        ).distinct()

    if busqueda_aviso:
        listaraviso = RegistroAviso.objects.filter(
            Q(Titulo_de_publicacion__icontains=busqueda_aviso) |
            Q(Descripcion__icontains=busqueda_aviso) |
            Q(Comuna__icontains=busqueda_aviso)
        ).distinct()

    data = {
        'listarusuario': listarusuario,
        'listaraviso': listaraviso,

    }
    return render(request, './administrador/panel.html', data)





#PUBLICACIONES

def registroaviso(request):
    data = {
        'form': RegistroAvisoForm(),

    }
    if request.method == 'POST':
        formulario = RegistroAvisoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "SE HA REGISTRADO EXITOSAMENTE."
        else:
            data['form'] = formulario
    return render(request, './publicaciones/registro.html', data)


def eliminaraviso(request, id):
    eliminaravisos = get_object_or_404(RegistroAviso, id=id)
    eliminaravisos.delete()
    return redirect(to="panel")

















