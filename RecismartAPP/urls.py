from django.urls import path
from .views import *

urlpatterns = [
    # SITIO

    path('', home, name="home"),
    path('login/', login, name="login"),
    path('test/', test, name="test"),
    path('tiporegistro/', tiporegistro, name="tiporegistro"),
    path('maspublicaciones/', maspublicaciones, name="maspublicaciones"),


    # CLIENTES

    path('registro/', registro, name="registro"),

    # RECOLECTOR

    path('registrorecolector/', registrorecolector, name="registrorecolector"),

    #ADMINISTRADOR
    path('panel/', panel, name="panel"),
    path('eliminaraviso/<id>/', eliminaraviso, name='eliminaraviso'),

    #PUBLICACION
    path('registroaviso/', registroaviso, name="registroaviso"),

]
