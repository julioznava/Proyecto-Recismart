# Generated by Django 4.1.4 on 2022-12-14 20:15

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Perfil_usuario', models.CharField(choices=[['Administrador', 'Administrador']], default='Administrador', max_length=100, verbose_name='Perfil de usuario')),
                ('Rut', models.CharField(max_length=100, unique=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('Telefono', models.CharField(max_length=100, unique=True)),
                ('Correo', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaRecolector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Perfil_usuario', models.CharField(choices=[['Recolector', 'Recolector']], default='Recolector', max_length=100, verbose_name='Perfil de usuario')),
                ('Rut', models.CharField(max_length=100, unique=True)),
                ('Rut_Empresa', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Nombre_de_empresa', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('Telefono', models.CharField(max_length=100, unique=True)),
                ('Correo', models.EmailField(max_length=100, unique=True)),
                ('Direccion', models.CharField(max_length=100)),
                ('Comuna', models.CharField(choices=[['Cerrillos', 'Cerrillos'], ['Cerro Navia', 'Cerro Navia'], ['Conchalí', 'Conchalí'], ['El Bosque', 'El Bosque'], ['Estación Central', 'Estación Central'], ['Huechuraba', 'Huechuraba'], ['Independencia', 'Independencia'], ['Cisterna', 'Cisterna'], ['La Florida', 'La Florida'], ['La Granja', 'La Granja'], ['La Pintana', 'La Pintana'], ['La Reina', 'La Reina'], ['Las Condes', 'Las Condes'], ['Lo Barnechea', 'Lo Barnechea'], ['Lo Espejo', 'Lo Espejo'], ['Lo Prado', 'Lo Prado'], ['Macul', 'Macul'], ['Maipú', 'Maipú'], ['Ñuñoa', 'Ñuñoa'], ['Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'], ['Peñalolén', 'Peñalolén'], ['Providencia', 'Providencia'], ['Pudahuel', 'Pudahuel'], ['Quilicura', 'Quilicura'], ['Quinta Normal', 'Quinta Normal'], ['Recoleta', 'Recoleta'], ['Renca', 'Renca'], ['Santiago', 'Santiago'], ['San Joaquín', 'San Joaquín'], ['San Miguel', 'San Miguel'], ['San Ramón', 'San Ramón'], ['Vitacura', 'Vitacura'], ['Puente Alto', 'Puente Alto'], ['Pirque', 'Pirque'], ['San José de Maipo', 'San José de Maipo'], ['Colina', 'Colina'], ['Lampa', 'Lampa'], ['Tiltil', 'Tiltil'], ['San Bernardo', 'San Bernardo'], ['Buin', 'Buin'], ['Calera de Tango', 'Calera de Tango'], ['Paine', 'Paine'], ['Melipilla', 'Melipilla'], ['Alhué', 'Alhué'], ['Curacaví', 'Curacaví'], ['María Pinto', 'María Pinto'], ['San Pedro', 'San Pedro'], ['Talagante', 'Talagante'], ['El Monte', 'El Monte'], ['Isla de Maipo', 'Isla de Maipo'], ['Padre Hurtado', 'Padre Hurtado'], ['Peñaflor', 'Peñaflor']], max_length=100)),
                ('Region', models.CharField(choices=[['Region Metropolitana', 'Region Metropolitana']], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Perfil_usuario', models.CharField(choices=[['Usuario', 'Usuario']], default='Usuario', max_length=100, verbose_name='Perfil de usuario')),
                ('Rut', models.CharField(max_length=100, unique=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('Telefono', models.CharField(max_length=100)),
                ('Correo', models.EmailField(max_length=100, unique=True)),
                ('Direccion', models.CharField(max_length=100)),
                ('Comuna', models.CharField(choices=[['Cerrillos', 'Cerrillos'], ['Cerro Navia', 'Cerro Navia'], ['Conchalí', 'Conchalí'], ['El Bosque', 'El Bosque'], ['Estación Central', 'Estación Central'], ['Huechuraba', 'Huechuraba'], ['Independencia', 'Independencia'], ['Cisterna', 'Cisterna'], ['La Florida', 'La Florida'], ['La Granja', 'La Granja'], ['La Pintana', 'La Pintana'], ['La Reina', 'La Reina'], ['Las Condes', 'Las Condes'], ['Lo Barnechea', 'Lo Barnechea'], ['Lo Espejo', 'Lo Espejo'], ['Lo Prado', 'Lo Prado'], ['Macul', 'Macul'], ['Maipú', 'Maipú'], ['Ñuñoa', 'Ñuñoa'], ['Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'], ['Peñalolén', 'Peñalolén'], ['Providencia', 'Providencia'], ['Pudahuel', 'Pudahuel'], ['Quilicura', 'Quilicura'], ['Quinta Normal', 'Quinta Normal'], ['Recoleta', 'Recoleta'], ['Renca', 'Renca'], ['Santiago', 'Santiago'], ['San Joaquín', 'San Joaquín'], ['San Miguel', 'San Miguel'], ['San Ramón', 'San Ramón'], ['Vitacura', 'Vitacura'], ['Puente Alto', 'Puente Alto'], ['Pirque', 'Pirque'], ['San José de Maipo', 'San José de Maipo'], ['Colina', 'Colina'], ['Lampa', 'Lampa'], ['Tiltil', 'Tiltil'], ['San Bernardo', 'San Bernardo'], ['Buin', 'Buin'], ['Calera de Tango', 'Calera de Tango'], ['Paine', 'Paine'], ['Melipilla', 'Melipilla'], ['Alhué', 'Alhué'], ['Curacaví', 'Curacaví'], ['María Pinto', 'María Pinto'], ['San Pedro', 'San Pedro'], ['Talagante', 'Talagante'], ['El Monte', 'El Monte'], ['Isla de Maipo', 'Isla de Maipo'], ['Padre Hurtado', 'Padre Hurtado'], ['Peñaflor', 'Peñaflor']], max_length=100)),
                ('Region', models.CharField(choices=[['Region Metropolitana', 'Region Metropolitana']], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100, unique=True, verbose_name='Titulo de la publicacion')),
                ('Descripcion', models.TextField(max_length=500, verbose_name='Descripcion de la publicacion')),
                ('Comuna', models.CharField(blank=True, choices=[['Cerrillos', 'Cerrillos'], ['Cerro Navia', 'Cerro Navia'], ['Conchalí', 'Conchalí'], ['El Bosque', 'El Bosque'], ['Estación Central', 'Estación Central'], ['Huechuraba', 'Huechuraba'], ['Independencia', 'Independencia'], ['Cisterna', 'Cisterna'], ['La Florida', 'La Florida'], ['La Granja', 'La Granja'], ['La Pintana', 'La Pintana'], ['La Reina', 'La Reina'], ['Las Condes', 'Las Condes'], ['Lo Barnechea', 'Lo Barnechea'], ['Lo Espejo', 'Lo Espejo'], ['Lo Prado', 'Lo Prado'], ['Macul', 'Macul'], ['Maipú', 'Maipú'], ['Ñuñoa', 'Ñuñoa'], ['Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'], ['Peñalolén', 'Peñalolén'], ['Providencia', 'Providencia'], ['Pudahuel', 'Pudahuel'], ['Quilicura', 'Quilicura'], ['Quinta Normal', 'Quinta Normal'], ['Recoleta', 'Recoleta'], ['Renca', 'Renca'], ['Santiago', 'Santiago'], ['San Joaquín', 'San Joaquín'], ['San Miguel', 'San Miguel'], ['San Ramón', 'San Ramón'], ['Vitacura', 'Vitacura'], ['Puente Alto', 'Puente Alto'], ['Pirque', 'Pirque'], ['San José de Maipo', 'San José de Maipo'], ['Colina', 'Colina'], ['Lampa', 'Lampa'], ['Tiltil', 'Tiltil'], ['San Bernardo', 'San Bernardo'], ['Buin', 'Buin'], ['Calera de Tango', 'Calera de Tango'], ['Paine', 'Paine'], ['Melipilla', 'Melipilla'], ['Alhué', 'Alhué'], ['Curacaví', 'Curacaví'], ['María Pinto', 'María Pinto'], ['San Pedro', 'San Pedro'], ['Talagante', 'Talagante'], ['El Monte', 'El Monte'], ['Isla de Maipo', 'Isla de Maipo'], ['Padre Hurtado', 'Padre Hurtado'], ['Peñaflor', 'Peñaflor']], max_length=100, null=True)),
                ('Region', models.CharField(blank=True, choices=[['Region Metropolitana', 'Region Metropolitana']], max_length=100, null=True)),
                ('Fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de la publicacion')),
                ('imagen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RecismartAPP.fotos', verbose_name='Imagenes de la publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecismartAPP.cuentausuario')),
            ],
        ),
    ]
