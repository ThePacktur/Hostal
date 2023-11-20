from django.contrib import admin
from hotelApp.models import Hotel
from hotelApp.models import Habitacion
from hotelApp.models import Pasajero

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(Pasajero)