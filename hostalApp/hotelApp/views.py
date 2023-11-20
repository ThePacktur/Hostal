from django.shortcuts import render, redirect, get_list_or_404
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
    
    return render(request, 'hotelApp/listadoHotel.html', {'hoteles':hoteles})

def crearHotel(request):
    if request.method == 'POST':
        form = HostalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaHotel')
    else:
        form = HostalForm()
    return render(request, 'hotelApp/crearHotel.html', {'form': form})

def editarHotel(request, id):
    hotel = get_list_or_404(Hotel, id=id)
    if request.method == 'POST':
        form = HostalForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('listaHotel')
    else:
        form = HostalForm(instance=hotel)
    return render(request, 'hotelApp/editarHotel.html', {'form': form, 'hotel': hotel})

def eliminarHotel(request, id):
    hotel = get_list_or_404(Hotel, id=id)
    hotel.delete()
    return redirect('listaHotel')

def listaHabitacion(request):    
    habitaciones = Habitacion.objects.all()
    
    return render(request, 'hotelApp/listadoHabitacion.html', {'habitaciones':habitaciones})

def crearHabitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaHabitacion')
    else:
        form = HabitacionForm()
    return render(request, 'hotelApp/crearHabitacion.html', {'form': form})

def editarHabitacion(request, habitacion_id):
    habitacion = get_list_or_404(Habitacion, pk=habitacion_id)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('listaHabitaciones')
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, 'hotelApp/editarHabitacion.html', {'form': form, 'habitacion': habitacion})

def eliminarHabitacion(request, habitacion_id):
    habitacion = get_list_or_404(Habitacion, pk=habitacion_id)
    habitacion.delete()
    return redirect('listaHabitaciones')
    

def listaPasajero(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'hotelApp/listadoPasajero.html', {'pasajeros': pasajeros})

def crearPasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaPasajeros')
    else:
        form = PasajeroForm()
    return render(request, 'hotelApp/crearPasajero.html', {'form': form})

def editarPasajero(request, pasajero_id):
    pasajero = get_list_or_404(Pasajero, pk=pasajero_id)
    if request.method == 'POST':
        form = PasajeroForm(request.POST, instance=pasajero)
        if form.is_valid():
            form.save()
            return redirect('listaPasajeros')
    else:
        form = PasajeroForm(instance=pasajero)
    return render(request, 'hotelApp/editarPasajero.html', {'form': form, 'pasajero': pasajero})


def eliminarPasajero(request, pasajero_id):
    pasajero = get_list_or_404(Pasajero, pk=pasajero_id)
    pasajero.delete()
    return redirect('listaPasajeros')