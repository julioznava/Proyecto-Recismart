from django.urls import path
from .views import *

urlpatterns = [
    # SITIO

    path('', home, name="home"),
    path('login/', login, name="login"),
    path('test/', test, name="test"),
    path('tiporegistro/', tiporegistro, name="tiporegistro"),


    # CLIENTES

    path('registro/', registro, name="registro"),

    # RECOLECTOR

    path('registrorecolector/', registrorecolector, name="registrorecolector"),

    #ADMINISTRADOR
    path('panel/', panel, name="panel"),


    #PUBLICACION
    path('registroaviso/', registroaviso, name="registroaviso"),


]