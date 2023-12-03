"""
URL configuration for hostalApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('listaHotel/', views.listaHotel, name='listarHotel'), 
    path('listaHabitacion/', views.listaHabitacion, name='listaHabitacion'),
    path('listaPasajero/', views.listaPasajero, name='listaPasajero'), 
    path('crearHotel/', views.crearHotel, name='crearHotel'),
    path('editarHotel/<int:id>/', views.editarHotel, name='editarHotel'),
    path('eliminarHotel/<int:id>/', views.eliminarHotel, name='eliminarHotel'),
    path('crearHabitacion/', views.crearHabitacion, name='crearHabitacion'),
    path('editarHabitacion/<int:habitacion_id>/', views.editarHabitacion, name='editarHabitacion'),
    path('eliminarHabitacion/<int:habitacion_id>/', views.eliminarHabitacion, name='eliminarHabitacion'),
    path('crearPasajero/', views.crearPasajero, name='crearPasajero'),
    path('editarPasajero/<int:pasajero_id>/', views.editarPasajero, name='editarPasajero'),
    path('eliminarPasajero/<int:pasajero_id>/', views.eliminarPasajero, name='eliminarPasajero'),
    path('pedirHabitacion', views.pedirHabitacion, name='pedirHabitacion')
]
