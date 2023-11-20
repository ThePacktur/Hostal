from django.shortcuts import render, redirect
from hotelApp.models import Hotel
from hotelApp.models import Habitacion
from hotelApp.models import Pasajero
from hotelApp.forms import HostalForm
from hotelApp.forms import PasajeroForm
from hotelApp.forms import HabitacionForm

# Create your views here.

def index(request):
    return render(request,'hotelApp/index.html')

def listadoHostal(request):
    hostal = Hotel.objects.all()
    data = {'hostal':hostal}
    return render(request, 'hotelApp/hotel.html',data)

def agregarHostal(request):
    form = HostalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listadoHostal')
    return render(request,'hotelApp/agregarHotel.html', {'form':form})


def eliminarHostal(request,id):
    hostal = Hotel.objects.get(id=id)
    hostal.delete()
    return redirect('listadoHostal')



def listadoHabitacion(request):
    habitacion = Habitacion.objects.all()
    data = {'habitacion':habitacion}
    return render(request,'hotelApp/habitaciones.html',data)

def agregarHabitacion(request):
    
    form = HabitacionForm(request.POST or None)
    if form.is_valid() and request.POST:
            form.save()
            return redirect('listadoHabitacion')
    return render(request, 'hotelApp/agregarHabitacion.html',{'form':form})

def eliminarHabitacion(request, id):
    habitacion = Habitacion.objects.get(id=id)
    habitacion.delete()
    return redirect('listadoHabitacion')


def listadoPasajero(request):
    pasajero = Pasajero.objects.all()   
    data = {'pasajero':pasajero}
    return render(request,'hotelApp/pasajero.html',data)



def agregarPasajero(request):
     form = HabitacionForm(request.POST or None)
     if form.is_valid():
            form.save()
            return redirect('listadoPasajero')
     return render(request, 'hotelApp/agregarPasajeros.html',{'form':form})


def eliminarPasajero(request,id):
    pasajeros = Pasajero.objects.get(id=id)
    pasajeros.delete()
    return redirect('listadoPasajero')

def actualizarHostal(request,id):
    hotel = Hotel.objects.get(id=id)
    form = HostalForm(request.POST or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listadoHostal')
    return render(request,'hotel/agregarHotel.html', {'form':form, 'hotel':hotel })

def actualizarPasajero(request,id):
    pasajero = Pasajero.objects.get(id=id)
    form = PasajeroForm(request.POST or None, instance=pasajero)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listadoPasajero')
    return render(request,'hotelApp/agregarPasajero.html', {'form':form, 'pasajero':pasajero })

def actualizarHabitacion(request, id):
    habitacion = HabitacionForm.objects.get(id=id)
    form = HabitacionForm(request.POST or None, instance=habitacion)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listadoHabitacion')
    return render(request,'hotelApp/agregarHabitacion.html', {'form':form, 'habitacion':habitacion })

    
