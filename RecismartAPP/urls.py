from django.urls import path
from .views import *

urlpatterns = [
    # SITIO

    path('', home, name="home"),
    path('login/', login, name="login"),
    path('test/', test, name="test"),
    path('maspublicaciones/', maspublicaciones, name="maspublicaciones"),


    # REGISTROS

    path('registro/', registro, name="registro"),
    path('modificarusuario/<id>/', modificarusuario, name="modificarusuario"),





    #ADMINISTRADOR
    path('panel/', panel, name="panel"),
    path('eliminaraviso/<id>/', eliminaraviso, name='eliminaraviso'),


    #PUBLICACION
    path('registroaviso/', registroaviso, name="registroaviso"),
]


