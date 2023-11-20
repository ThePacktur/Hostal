from django.db import models

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombreHotel = models.CharField(max_length=20)
    direccionHotel = models.CharField(max_length=20)
    habitacionHotel = models.IntegerField()
    tarifaHotel = models.FloatField()
    phoneHotel = models.CharField(max_length=20)
    numberHotel = models.IntegerField()

    def __str__(self):
        return self.nombreHotel


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
    apellidoClient = models.CharField(max_length=20)
    fonoClient = models.CharField(max_length=30)
    llegadaClient = models.CharField(max_length=20)
    salidaClient = models.CharField(max_length=20)

    def __str__(self):
        return self.rutClient