# Generated by Django 4.2.6 on 2023-12-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0006_remove_pasajero_pedir_alter_habitacion_capacidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='llegadaClient',
            field=models.DateTimeField(verbose_name='Día de llega'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='salidaClient',
            field=models.DateTimeField(verbose_name='Dia de salida'),
        ),
    ]