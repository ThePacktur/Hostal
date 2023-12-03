from django.db import models
#Source
#https://www.youtube.com/watch?v=hX8Mcj3-8hk&t=190s
# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombreHotel = models.CharField(max_length=255, verbose_name='Nombre del hotel')
    direccionHotel = models.CharField(max_length=255, verbose_name='Direccion del hotel')
    numberHotel = models.IntegerField(verbose_name="Numero de la direccion del hotel")
    habitacionHotel = models.IntegerField(verbose_name='Numero de habitaciones')
    tarifaHotel = models.FloatField(verbose_name='Tarifa del hotel')
    phoneHotel = models.CharField(max_length=15, verbose_name='Numero de telefono del hotel')
    
    def __str__(self):
        return f'{self.nombreHotel} - {self.direccionHotel} #{self.numberHotel}'

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    idHotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Dirección del Hotel'
    )
    habitacion = models.CharField(max_length=255, verbose_name='Numero de la habitacion')
    capacidad = models.IntegerField(verbose_name='Capacidad de la habitacion')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de la habitacion')
    terraza = models.BooleanField(verbose_name='¿Hay terraza?')
    cocina = models.BooleanField(verbose_name='¿Hay cocina?')  
    disponibilidad = models.BooleanField('¿Esta disponible?')
    
    def __str__(self):
        return self.habitacion

class Pasajero(models.Model):
    id = models.AutoField(primary_key=True)
    rutClient = models.CharField(max_length=15, verbose_name='Rut')
    nombreClient = models.CharField(max_length=255, verbose_name='Nombre')
    apellidoClient = models.CharField(max_length=255, verbose_name='Apellido')
    fonoClient = models.CharField(max_length=15, verbose_name='Numero telefonico')
    llegadaClient = models.CharField(max_length=23, verbose_name='Día de llega')
    salidaClient = models.CharField(max_length=23, verbose_name='Dia de salida')

    def __str__(self):
        return self.rutClient
    
class PasajeroHabitacion(models.Model):
    id = models.AutoField(primary_key=True)
    pasajero = models.ForeignKey(
        Pasajero,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Nombre del Pasajero'
    )
    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Numero de habitacion'
    )
    hotel=models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Direccion'
    )
    
    class meta:
        db_table = 'pasajero_pasajero_habitacion'
        verbose_name = "habitacion pasajero"
        verbose_name_plura = 'Habitaciones Pasajeros'
        
    def __str__(self) :
        return f"{self.id} {self.habitacion.id}"
    