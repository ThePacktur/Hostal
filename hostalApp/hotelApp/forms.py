from django import forms
from hotelApp.models import Hotel   
from hotelApp.models import Habitacion
from hotelApp.models import Pasajero
from hotelApp.models import PasajeroHabitacion

class HostalForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'
        
#class HabitacionForm(forms.ModelForm):
#    direccion = forms.ModelChoiceField(queryset=Hotel.objects.all(), required=False, label='Dirección del Hotel')
#
#    class Meta:
#        model = Habitacion
#        fields = '__all__'
#        ['habitacion', 'capacidad', 'precio', 'terraza', 'cocina', 'disponibilidad']

class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = '__all__'

class PasajeroHabitacionForm(forms.ModelForm):
    class Meta:
        model = PasajeroHabitacion
        fields = '__all__'