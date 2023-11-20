from django.db import models

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    direccionHotel = models.CharField(max_length=255)
    nombreHotel = models.CharField(max_length=255)
    habitacionHotel = models.IntegerField()
    tarifaHotel = models.FloatField()
    phoneHotel = models.CharField(max_length=15)
    numberHotel = models.IntegerField()
  
    
    def __str__(self):
        return self.nombreHotel

class Habitacion(models.Model):
    
    habitacion = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    terraza = models.BooleanField()
    cocina = models.BooleanField()  
    disponibilidad = models.BooleanField()
    
    def __str__(self):
        return self.habitacion

class Pasajero(models.Model):
    rutClient = models.CharField(max_length=15)
    nombreClient = models.CharField(max_length=255)
    apellidoClient = models.CharField(max_length=255)
    fonoClient = models.CharField(max_length=15)
    llegadaClient = models.CharField(max_length=23)
    salidaClient = models.CharField(max_length=23)

    def __str__(self):
        return self.rutClient