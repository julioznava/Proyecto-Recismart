from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from.forms import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login
from django.contrib import messages


#SITIO
def home(request):
    foto = Fotos.objects.all()

    context = {
        'foto':foto,
    }
    return render(request, './sitio/home.html', context)

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

    context = {
        'listaraviso': listaraviso,
    }
    return render(request, './sitio/maspublicaciones.html', context)


def panelayuda(request):
    return render(request, './sitio/ayuda.html')


def panelregistro(request):
    return render(request, './sitio/panelregistro.html')


#USUARIOS
def registrousuario(request):
    context = {
        'form': CuentaUsuarioForm()
    }
    if request.method == 'POST':
        formulario = CuentaUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Te has registrado exitosamente! Nuestros administradores revisaran tu solicitud de ingreso y te enviaremos un mail con las credenciales de acceso al correo que has registrado.')
            return redirect(to="home")

        context['form'] = formulario
    return render(request, './clientes/registro.html', context)


def modificarusuario(request, id):
    modificar_user = get_object_or_404(CuentaUsuario, id=id)

    context = {
        'form':CuentaUsuarioForm(instance=modificar_user)
    }
    if request.method == 'POST':
        formulario = CuentaUsuarioForm(data=request.POST, instance=modificar_user)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'EL USUARIO SE HA MODIFICADO EXITOSAMENTE.'

        return redirect(to="panel")
        context["form"] = formulario

    return render(request, './clientes/modificar.html', context)



# RECOLECTORES

def registrorecolector(request):
    context = {
        'form': CuentaRecolectorForm()
    }
    if request.method == 'POST':
        formulario = CuentaRecolectorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Te has registrado exitosamente! Nuestros administradores revisaran tu solicitud de ingreso y te enviaremos un mail con las credenciales de acceso al correo que has registrado.')
            return redirect(to="home")

        context['form'] = formulario
    return render(request, './recoletores/registrorecolector.html', context)


# ADMINISTRADOR


def reportes(request):
    return render(request, './administrador/reportes.html')


def registrocuenta(request):
    context = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            dj_login(request, user)
            messages.success(request, 'Se ha realizado la activación de la cuenta exitosamente..')
            return redirect(to="panel")

        context['form'] = formulario
    return render(request, './administrador/registrocuenta.html', context)



def registroadministrador(request):
    context = {
        'form': CuentaAdminForm()
    }
    if request.method == 'POST':
        formulario = CuentaAdminForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se ha realizado la el registro de la cuenta administrador exitosamente..')
            return redirect(to="home")

        context['form'] = formulario
    return render(request, './clientes/registro.html', context)

def panel(request):
    busqueda_usuario = request.GET.get("busqueda_usuario")
    busqueda_recolector = request.GET.get("busqueda_recolector")
    busqueda_aviso = request.GET.get("busqueda_aviso")

    listarusuario = CuentaUsuario.objects.all()
    listarecolector = CuentaRecolector.objects.all()
    listaraviso = RegistroAviso.objects.all()

    total_listarusuario = listarusuario.count()
    total_listarecolector = listarecolector.count()
    total_listaraviso = listaraviso.count()

    if busqueda_usuario:
        listarusuario = CuentaUsuario.objects.filter(
            Q(Perfil_usuario__icontains=busqueda_usuario) |
            Q(Rut__icontains=busqueda_usuario) |
            Q(Nombre__icontains=busqueda_usuario) |
            Q(Apellido__icontains=busqueda_usuario) |
            Q(Correo__icontains=busqueda_usuario) |
            Q(Comuna__icontains=busqueda_usuario)
        ).distinct()

    if busqueda_recolector:
        listarecolector = CuentaRecolector.objects.filter(
            Q(Perfil_usuario__icontains=busqueda_recolector) |
            Q(Rut__icontains=busqueda_recolector) |
            Q(Rut_Empresa__icontains=busqueda_recolector) |
            Q(Nombre__icontains=busqueda_recolector) |
            Q(Apellido__icontains=busqueda_recolector) |
            Q(Correo__icontains=busqueda_recolector) |
            Q(Comuna__icontains=busqueda_recolector)
        ).distinct()

    if busqueda_aviso:
        listaraviso = RegistroAviso.objects.filter(
            Q(Titulo_de_publicacion__icontains=busqueda_aviso) |
            Q(Descripcion__icontains=busqueda_aviso) |
            Q(Comuna__icontains=busqueda_aviso)
        ).distinct()

    context = {
        'listarusuario': listarusuario,
        'listaraviso': listaraviso,
        'listarecolector': listarecolector,
        'total_listarusuario': total_listarusuario,
        'total_listarecolector': total_listarecolector,
        'total_listaraviso': total_listaraviso,
    }
    return render(request, './administrador/panel.html', context)


def eliminarusuario(request, id):

    eliminarusuario = get_object_or_404(CuentaUsuario, id=id)
    eliminarusuario.delete()
    messages.success(request, 'Usuario eliminado exitosamente')
    return redirect(to="panel")



def eliminarecolector(request, id):

    eliminarecolector = get_object_or_404(CuentaRecolector, id=id)
    eliminarecolector.delete()
    messages.success(request, 'Recolector eliminado exitosamente')
    return redirect(to="panel")

def eliminarpublicacion(request, id):

    eliminarpublicacion = get_object_or_404(RegistroAviso, id=id)
    eliminarpublicacion.delete()
    messages.success(request, 'Publicacion eliminada exitosamente')
    return redirect(to="panel")


#PUBLICACIONES

def registroaviso(request):
    public = RegistroAviso.objects.all()

    context = {
        'form': RegistroAvisoForm(),
        'public': public,
    }
    if request.method == 'POST':
        formulario = RegistroAvisoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Tu publicación ha sido registrado exitosamente!. Nuestros administradores revisaran tu solicitud y en breves minutos será aprobada.')
            return redirect(to='home')
        else:
            context['form'] = formulario

    return render(request, './publicaciones/registro.html', context)



def subirfoto(request):
    if request.method == 'POST':
        formulario = FotosForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()

    cargasfotos = Fotos.objects.all()
    formulario = FotosForm()

    context = {
        'formulario': formulario,
        'cargasfotos': cargasfotos,
    }
    return render(request, './subidafoto.html', context)








