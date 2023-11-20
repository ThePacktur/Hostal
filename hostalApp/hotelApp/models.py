from django.db import models

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    NombreHostal = models.CharField(max_length=20)
    direccionHostal = models.CharField(max_length=20)
    habitacionHostal = models.IntegerField()
    tarifaHostal = models.FloatField()
    phoneHostal = models.CharField(max_length=20)
    numberHostal = models.IntegerField()

    def __str__(self):
        return self.nameHostal


class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    habitacion = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    precio = models.FloatField()
    terraza = models.CharField(max_length=20)
    cocina = models.CharField(max_length=20)
    disponibilidad = models.CharField(max_length=20)
    def __str__(self):
        return  self.habitacion
        

class Pasajero(models.Model):
    id = models.AutoField(primary_key=True)
    rutClient = models.CharField(max_length=20)
    nombreClient = models.CharField(max_length=20)
    apeliidoClint = models.CharField(max_length=20)
    fonoClient = models.CharField(max_length=30)
    llegadaClient = models.DateField(max_length=20)
    salidaClient = models.DateField(max_length=20)

    def __str__(self):
        return self.rutClient