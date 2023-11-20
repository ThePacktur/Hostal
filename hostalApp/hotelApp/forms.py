from django import forms
from .models import Hotel   
from .models import Habitacion
from .models import Pasajero

class HostalForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'

class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = '__all__'
