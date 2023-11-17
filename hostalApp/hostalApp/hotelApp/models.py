from django.db import models

# Create your models here.

class Hostal(models.Model):
    id = models.AutoField(primary_key=True)
    nameHostal = models.CharField(max_length=20)
    direccionHostal = models.CharField(max_length=20)
    habitacionHostal = models.IntegerField()
    tarifaHostal = models.FloatField()
    phoneHostal = models.CharField(max_length=20)
    numberHostal = models.IntegerField()

    def __str__(self):
        return self.nameHostal


class Habitacion(models.Model):
        
    pass

class Pasajero(models.Model):
    rutClient = models.CharField(max_length=20)
    nombreClient = models.CharField(max_length=20)
    apeliidoClint = models.CharField(max_length=20)
    fonoClient = models.CharField(max_length=30)
    llegadaClient = models.DateField()
    salidaClient = models.DateField()

    def __str__(self):
        return self.rutClient