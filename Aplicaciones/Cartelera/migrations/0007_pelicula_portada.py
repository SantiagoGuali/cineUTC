# Generated by Django 4.0.6 on 2024-06-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0006_alter_pelicula_duracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='portada',
            field=models.FileField(blank=True, null=True, upload_to='generos'),
        ),
    ]
