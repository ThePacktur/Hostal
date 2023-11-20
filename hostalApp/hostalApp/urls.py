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
    path('hoteles/', views.listadoHostal, name='hoteles'),
    path('habitaciones/', views.listadoHabitacion, name='habitaciones'),
    path('pasajeros/', views.listadoPasajero, name='pasajeros'),
    path("agregarHostal/", views.agregarHostal, name='agregarHostal'),
    path('agregarHabitacion/', views.agregarHabitacion, name='agregarHabitacion'),
    path('agregarPasajero/', views.agregarPasajero, name='agregarPasajero'),
    path('eliminarHostal/<int:id>/', views.eliminarHostal, name='eliminarHostal'),
    path('eliminarHabitacion/<int:id>/', views.eliminarHabitacion, name='eliminarHabitacion'),
    path('eliminarPasajero/<int:id>/', views.eliminarPasajero, name='eliminarPasajero'),
    path('actualizarHostal/<int:id>/', views.actualizarHostal, name='actializarHostal'),
    path('actualizarHabitacion/<int:id>/', views.actualizarHabitacion, name='actualizarHabitacion'),
    path('actualizarPasajero/<int:id>/', views.actualizarPasajero, name='actualizarPasajero'),
]
