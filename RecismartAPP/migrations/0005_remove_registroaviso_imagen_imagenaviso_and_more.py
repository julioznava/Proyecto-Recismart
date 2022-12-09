# Generated by Django 4.1.4 on 2022-12-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0004_registroaviso_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroaviso',
            name='imagen',
        ),
        migrations.CreateModel(
            name='ImagenAviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagen', models.ImageField(upload_to='productos')),
                ('RegistroAviso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecismartAPP.registroaviso')),
            ],
        ),
        migrations.AddField(
            model_name='registroaviso',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='publicacion'),
        ),
    ]
