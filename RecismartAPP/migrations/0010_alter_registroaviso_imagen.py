# Generated by Django 4.1.4 on 2022-12-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0009_alter_registroaviso_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroaviso',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='publicacion'),
        ),
    ]
