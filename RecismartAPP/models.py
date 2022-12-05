from django.db import models

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

class Comunas(models.Model):
    Comuna = models.CharField(max_length=100, choices=LISTA_COMUNAS_RM)

    def __str__(self):
        return self.Comuna


class Regiones(models.Model):
    Region = models.CharField(max_length=100, choices=LISTA_REGIONES)

    def __str__(self):
        return self.Region

class CuentaUsuario(models.Model):
    Rut = models.CharField(max_length=100, unique=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo_electronico = models.EmailField(max_length=50)
    Telefono = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Comuna = models.ForeignKey(Comunas, on_delete=models.CASCADE)
    Region = models.ForeignKey(Regiones, on_delete=models.CASCADE)

    def __str__(self):
        return self.Rut


class CuentaRecolector(models.Model):
    Rut_Empresa = models.CharField(max_length=100, unique=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo_electronico = models.EmailField(max_length=50)
    Telefono = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Nombre_de_empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre_de_empresa


class RegistroAviso(models.Model):
    Titulo_de_publicacion = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=300)
    Comuna = models.ForeignKey(Comunas, on_delete=models.CASCADE)
    Region = models.ForeignKey(Regiones, on_delete=models.CASCADE)


