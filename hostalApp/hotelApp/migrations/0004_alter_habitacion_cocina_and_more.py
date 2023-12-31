# Generated by Django 4.2.5 on 2023-11-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0003_rename_nombrehostal_hotel_direccionhotel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='cocina',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='disponibilidad',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='habitacion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='terraza',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='direccionHotel',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='nombreHotel',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phoneHotel',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='apellidoClient',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='fonoClient',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='llegadaClient',
            field=models.CharField(max_length=23),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='nombreClient',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='rutClient',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='salidaClient',
            field=models.CharField(max_length=23),
        ),
    ]
