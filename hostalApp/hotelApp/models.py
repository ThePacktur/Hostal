from django.db import models
#Source
#https://www.youtube.com/watch?v=hX8Mcj3-8hk&t=190s
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
        return f'{self.nombreHotel} - {self.direccionHotel}'

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    idHotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Dirección del Hotel'
    )
    habitacion = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    terraza = models.BooleanField()
    cocina = models.BooleanField()  
    disponibilidad = models.BooleanField()
    
    def __str__(self):
        return f"{self.habitacion} - {self.idHotel.direccionHotel if self.idHotel else 'Sin dirección'}"

class Pasajero(models.Model):
    id = models.AutoField(primary_key=True)
    rutClient = models.CharField(max_length=15)
    nombreClient = models.CharField(max_length=255)
    apellidoClient = models.CharField(max_length=255)
    fonoClient = models.CharField(max_length=15)
    llegadaClient = models.CharField(max_length=23)
    salidaClient = models.CharField(max_length=23)
    pedir = models.ManyToManyField(
        Habitacion,
        through="PasajeroHabitacion",
        blank=True
    )

    def __str__(self):
        return self.rutClient
    
class PasajeroHabitacion(models.Model):
    id = models.AutoField(primary_key=True)
    pasajero = models.ForeignKey(
        Pasajero,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    hotel=models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    class meta:
        db_table = 'pasajero_pasajero_habitacion'
        verbose_name = "habitacion pasajero"
        verbose_name_plura = 'Habitaciones Pasajeros'
        
    def __str__(self) :
        return f"{self.id} {self.habitacion.id}"
    