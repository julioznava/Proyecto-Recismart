from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from.forms import *
from django.db.models import Q
from django.contrib import messages


# TESTING

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.core.mail import EmailMessage # TESTING
# from .token import account_activation_token # TESTING


#SITIO
def home(request):
    return render(request, './sitio/home.html')

def login(request):
    return render(request, './registration/login.html')


def test(request):
    return render(request, './testing/test.html')


def tiporegistro(request):
    return render(request, './sitio/tiporegistro.html')


def maspublicaciones(request):
    return render(request, './sitio/maspublicaciones.html')

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


















# TESTING



# def activate(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user =User.object.get(pk=uid)
#     except:
#         User = None
#
#     if User is not None and account_activation_token.check_token(user, token):
#         User.is_active = True
#         user.save()
#
#         messages.success(request, "Gracias por su confirmacion al sitio, ahora podra logearse con su cuenta de acceso")
#         return redirect('login')
#     else:
#         messages.error(request, "El link de activacion es invalido")
#
#     return redirect('home')


# def activatemail(request, user, to_email):
#     mail_subject = "Activar tu cuenta de usuario"
#     message = render_to_string("template_activate_account.html", {
#         'user': user.username,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_decode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#         "protocol": 'https' if request.is_secure() else 'http'
#      })


#     email = EmailMessage(mail_subject, message, to=[to_email])
#     if email.send():
#         messages.success(request, f'Estimado <b>{user}<b>, por favor dirijase a su correo <b>{to_email}<b> y en su bandeja de entrada\
#          recibira el link de activacion para que confirme el registro. <b>Nota:<b> Tambien chequee su bandeja de SPAM.')
#     else:
#         message.error(request, f'Si aun no ha recibido el mensaje al correo:  {to_email},Por favor corrobore que el correo ha sido escrito correctamente. ')
#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm()
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             activateEmail(request, user, form.cleaned_data.get('email'))
#             return redirect('login')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST'
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            return  redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request,error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name='testing/register.html',
        context={'form':form}
    )