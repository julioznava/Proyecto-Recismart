# Generated by Django 4.1.4 on 2022-12-11 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0021_registropersonas_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registropersonas',
            name='Correo',
        ),
    ]