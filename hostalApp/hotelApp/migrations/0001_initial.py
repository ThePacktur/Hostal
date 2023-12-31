# Generated by Django 4.2.5 on 2023-11-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('habitacion', models.CharField(max_length=20)),
                ('capacidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('terraza', models.CharField(max_length=20)),
                ('cocina', models.CharField(max_length=20)),
                ('disponibilidad', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hostal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameHostal', models.CharField(max_length=20)),
                ('direccionHostal', models.CharField(max_length=20)),
                ('habitacionHostal', models.IntegerField()),
                ('tarifaHostal', models.FloatField()),
                ('phoneHostal', models.CharField(max_length=20)),
                ('numberHostal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rutClient', models.CharField(max_length=20)),
                ('nombreClient', models.CharField(max_length=20)),
                ('apeliidoClint', models.CharField(max_length=20)),
                ('fonoClient', models.CharField(max_length=30)),
                ('llegadaClient', models.DateField(max_length=20)),
                ('salidaClient', models.DateField(max_length=20)),
            ],
        ),
    ]
