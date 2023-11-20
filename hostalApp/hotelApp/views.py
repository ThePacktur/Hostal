from django.shortcuts import render, redirect
from hotelApp.models import Hotel
from hotelApp.forms import HostalForm
from hotelApp.models import Habitacion
from hotelApp.forms import HabitacionForm
from hotelApp.models import Pasajero
from hotelApp.forms import PasajeroForm


# Create your views here.

def index(request):
    return render(request,'hotelApp/index.html')

def listaHotel(request):    
    hoteles = Hotel.objects.all()
    
    return render(request, 'hotelApp/listadoHotel.html',{'hoteles':hoteles})

def crearHotel(request):
    form = HostalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaHotel')
    return render(request, 'hotelApp/crearHotel.html', {'form':form})

def editarHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    form = HostalForm(request.POST or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listaHotel')
    return render(request,'hotelApp/editarHotel.html', {'form':form, 'hotel':hotel })

def eliminarHotel(request,id):
    hotel = Hotel.objects.get(id=id)
    hotel.delete()
    return redirect('listaHotel')

def listaHabitacion(request):    
    habitaciones = Habitacion.objects.all()
    
    return render(request, 'hotelApp/listadoHabitacion.html',{'habitaciones':habitaciones})

def crearHabitacion(request):
    form = HabitacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaHabitacion')
    return render(request, 'hotelApp/crearHabitacion.html', {'form':form})

def editarHabitacion(request, id):
    habitaciones = Habitacion.objects.get(id=id)
    form = HabitacionForm(request.POST or None, instance=habitaciones)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listahabitacion')
    return render(request,'hoteles/editarHabitacion.html', {'form':form, 'habitaciones':habitaciones })

def eliminarHabitacion(request, id):
    habitacion = Habitacion.objects.get(id=id)
    habitacion.delete()
    return redirect('listaHabitacion')

    

def listaPasajero(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'hotelApp/listadoPasajero.html', {'pasajeros': pasajeros})

def crearPasajero(request):
    form = PasajeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaPasajero')
    return render(request, 'hotelApp/crearPasajero.html', {'form':form})

def editarPasajero(request, id):
    pasajeros = Pasajero.objects.get(id=id)
    form = PasajeroForm(request.POST or None, instance=pasajeros)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listaPasajero')
    return render(request,'hotelApp/editarPasajero.html', {'form':form, 'pasajeros':pasajeros })

def eliminarPasajero(request, id):
    pasajeros = Pasajero.objects.get(id=id)
    pasajeros.delete()
    return redirect('listaPasajero')
