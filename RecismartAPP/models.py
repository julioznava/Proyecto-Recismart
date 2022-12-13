from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.


LISTA_REGIONES = [
    ['Region Metropolitana', 'Region Metropolitana'],
]

LISTA_COMUNAS_RM = [
    ['Cerrillos','Cerrillos'],
    ['Cerro Navia','Cerro Navia'],
    ['Conchalí','Conchalí'],
    ['El Bosque','El Bosque'],
    ['Estación Central','Estación Central'],
    ['Huechuraba','Huechuraba'],
    ['Independencia','Independencia'],
    ['Cisterna','Cisterna'],
    ['La Florida','La Florida'],
    ['La Granja','La Granja'],
    ['La Pintana','La Pintana'],
    ['La Reina','La Reina'],
    ['Las Condes','Las Condes'],
    ['Lo Barnechea','Lo Barnechea'],
    ['Lo Espejo','Lo Espejo'],
    ['Lo Prado','Lo Prado'],
    ['Macul','Macul'],
    ['Maipú','Maipú'],
    ['Ñuñoa','Ñuñoa'],
    ['Pedro Aguirre Cerda','Pedro Aguirre Cerda'],
    ['Peñalolén','Peñalolén'],
    ['Providencia','Providencia'],
    ['Pudahuel','Pudahuel'],
    ['Quilicura','Quilicura'],
    ['Quinta Normal','Quinta Normal'],
    ['Recoleta','Recoleta'],
    ['Renca','Renca'],
    ['Santiago','Santiago'],
    ['San Joaquín','San Joaquín'],
    ['San Miguel','San Miguel'],
    ['San Ramón','San Ramón'],
    ['Vitacura','Vitacura'],
    ['Puente Alto','Puente Alto'],
    ['Pirque','Pirque'],
    ['San José de Maipo','San José de Maipo'],
    ['Colina','Colina'],
    ['Lampa','Lampa'],
    ['Tiltil','Tiltil'],
    ['San Bernardo','San Bernardo'],
    ['Buin','Buin'],
    ['Calera de Tango','Calera de Tango'],
    ['Paine','Paine'],
    ['Melipilla','Melipilla'],
    ['Alhué','Alhué'],
    ['Curacaví','Curacaví'],
    ['María Pinto','María Pinto'],
    ['San Pedro','San Pedro'],
    ['Talagante','Talagante'],
    ['El Monte','El Monte'],
    ['Isla de Maipo','Isla de Maipo'],
    ['Padre Hurtado','Padre Hurtado'],
    ['Peñaflor','Peñaflor'],

]

TIPO_ADMINISTRADOR = [
    ['Administrador', 'Administrador'],
]

TIPO_USUARIO = [
    ['Usuario', 'Usuario'],
]

TIPO_RECOLECTOR = [
    ['Recolector', 'Recolector'],
]


class Fotos(models.Model):
    image = CloudinaryField('image')


class CuentaUsuario(models.Model):
    Perfil_usuario = models.CharField(max_length=100, choices=TIPO_USUARIO, default='Usuario', verbose_name='Perfil de usuario')
    Rut = models.CharField(max_length=100, unique=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    Telefono = models.CharField(max_length=100)
    Correo = models.EmailField(max_length=100, unique=True)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100, choices=LISTA_COMUNAS_RM)
    Region = models.CharField(max_length=100, choices=LISTA_REGIONES)

    def __str__(self):
        return self.Rut

class CuentaRecolector(models.Model):
    Perfil_usuario = models.CharField(max_length=100, choices=TIPO_RECOLECTOR, default='Recolector', verbose_name='Perfil de usuario')
    Rut = models.CharField(max_length=100, unique=True)
    Rut_Empresa = models.CharField(max_length=100, unique=True, null=True, blank=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Nombre_de_empresa = models.CharField(max_length=100, unique=True, null=True, blank=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    Telefono = models.CharField(max_length=100, unique=True)
    Correo = models.EmailField(max_length=100, unique=True)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100, choices=LISTA_COMUNAS_RM)
    Region = models.CharField(max_length=100, choices=LISTA_REGIONES)


    def __str__(self):
        return self.Rut

class CuentaAdmin(models.Model):
    Perfil_usuario = models.CharField(max_length=100, choices=TIPO_ADMINISTRADOR, default='Administrador', verbose_name='Perfil de usuario')
    Rut = models.CharField(max_length=100, unique=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    Telefono = models.CharField(max_length=100, unique=True)
    Correo = models.EmailField(max_length=100, unique=True)


    def __str__(self):
        return self.Rut


class RegistroAviso(models.Model):
    Titulo = models.CharField(max_length=100, unique=True, verbose_name='Titulo de la publicacion')
    Descripcion = models.TextField(max_length=500, verbose_name='Descripcion de la publicacion')
    Comuna = models.CharField(max_length=100, choices=LISTA_COMUNAS_RM, blank=True, null=True)
    Region = models.CharField(max_length=100, choices=LISTA_REGIONES, blank=True, null=True)
    Fecha_publicacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de la publicacion')
    imagen = models.ForeignKey(Fotos, on_delete=models.CASCADE, blank= True, null=True, verbose_name='Imagenes de la publicacion')

    def __str__(self):
        return self.Titulo

