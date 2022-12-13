from django.urls import path
from .views import *

urlpatterns = [
    # SITIO

    path('', home, name="home"),
    path('login/', login, name="login"),
    path('test/', test, name="test"),
    path('maspublicaciones/', maspublicaciones, name="maspublicaciones"),
    path('panelayuda/', panelayuda, name="panelayuda"),
    path('panelregistro/', panelregistro, name="panelregistro"),


    # REGISTROS

    path('registrousuario/', registrousuario, name="registrousuario"),
    path('modificarusuario/<id>/', modificarusuario, name="modificarusuario"),
    path('registrorecolector/', registrorecolector, name="registrorecolector"),
    path('registroadministrador/', registroadministrador, name="registroadministrador"),





    #ADMINISTRADOR
    path('panel/', panel, name="panel"),
    path('eliminaraviso/<id>/', eliminaraviso, name='eliminaraviso'),
    path('modificarusuario/<id>/', modificarusuario, name="modificarusuario"),
    path('registrocuenta/', registrocuenta, name="registrocuenta"),


    #PUBLICACION
    path('registroaviso/', registroaviso, name="registroaviso"),


    # SUBIDAFOTO (TEST)
    path('subirfoto/', subirfoto, name="subirfoto"),

]