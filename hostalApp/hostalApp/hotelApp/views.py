from django.shortcuts import render, redirect
from hotelApp.models import Hostal
from hotelApp.models import Habitacion
from hotelApp.models import Pasajero
# Create your views here.

def index(request):
    return render(request,'index.html')

def listadoHostal(request):
    hostal = Hostal.objects.all()
    date = {'hostal': hostal}
    return render(request, 'hoteles.html')

def listadoHabitacion():
    pass

def listadoPasajero():
    pass

def agregarHostal():
    pass

def agregarHabitacion():
    pass

def agregarPasajero():
    pass

def eliminarHostal():
    pass

def eliminarHabitacion():
    pass

def eliminarPasajero():
    pass

def actualizarHostal():
    pass

def actualizarPasajero():
    pass

def actualizarHabitacion():
    pass
