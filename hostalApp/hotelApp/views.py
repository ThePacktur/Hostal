from django.shortcuts import render, redirect, get_list_or_404
from hotelApp.models import Hotel
from hotelApp.forms import HostalForm
from hotelApp.models import Habitacion
from hotelApp.forms import HabitacionForm
from hotelApp.models import Pasajero
from hotelApp.forms import PasajeroForm
from hotelApp.models import PasajeroHabitacion
from hotelApp.forms import PasajeroHabitacionForm


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
            return redirect('/listaHotel')
    else:
        form = HostalForm()
    return render(request, 'hotelApp/crearHotel.html', {'form': form})

def editarHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    form = HostalForm(request.POST or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('/listaHotel')
    return render(request,'hotelApp/editarHotel.html', {'form':form, 'hotel':hotel })

def eliminarHotel(request,id):
    hotel = Hotel.objects.get(id=id)
    hotel.delete()
    return redirect('/listaHotel')

def listaHabitacion(request):    
    habitaciones = Habitacion.objects.all()
    hoteles = Hotel.objects.all()
    return render(request, 'hotelApp/listadoHabitacion.html', {'habitaciones':habitaciones, 'hoteles':hoteles})

def crearHabitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listaHabitacion')
    else:
        form = HabitacionForm()
    return render(request, 'hotelApp/crearHabitacion.html', {'form': form})

def editarHabitacion(request, id):
    habitacion = HabitacionForm.objects.get(id=id)
    form = HostalForm(request.POST or None, instance=habitacion)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('/listaHabitacion')
    return render(request,'hotelApp/editarHabitacion.html', {'form':form, 'habitacion':habitacion })


def eliminarHabitacion(request,id):
    habitacion = Habitacion.objects.get(id=id)
    habitacion.delete()
    return redirect('listaHabitacion')    

def listaPasajero(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'hotelApp/listadoPasajero.html', {'pasajeros': pasajeros})

def crearPasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listaPasajero')
    else:
        form = PasajeroForm()
    return render(request, 'hotelApp/crearPasajero.html', {'form': form})

def editarPasajero(request, id):
    pasajero =  Pasajero.objects.get(id=id)
    form = PasajeroForm(request.POST or None, instance=pasajero)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('/listaPasajeros')
    return render(request, 'hotelApp/editarPasajero.html', {'form': form, 'pasajero': pasajero})

def editarHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    form = HostalForm(request.POST or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('/listaHotel')
    return render(request,'hotelApp/editarHotel.html', {'form':form, 'hotel':hotel })

def eliminarPasajero(request, id):
    pasajero = Pasajero.objects.get(id=id)
    pasajero.delete()
    return redirect('/listaPasajero/')


def pedirHabitacion(request):
    if request.method == 'POST':
        form = PasajeroHabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadoPedido')
    else:
        form = PasajeroHabitacionForm()
    return render(request, 'hotelApp/pedirHabitacion.html', {'form': form})

def listaPedido(request):
    pedido = PasajeroHabitacion.objects.all()
    return render(request, 'hotelApp/listadoPedido.html', {'PasajeroHabitacion': pedido})

def editaPedido(request, id):
    pedido = PasajeroHabitacion.objects.get(id=id)
    form = PasajeroHabitacionForm(request.POST or None, instance=pedido)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('/listadoPedido')
    return render(request,'hotelApp/editarPedido.html', {'form':form, 'PasajeroHabitacion':pedido })

def eliminarPedido(request, id):
    pedido = PasajeroHabitacion.objects.get(id=id)
    pedido.delete()
    return redirect('/listadoPedido/')