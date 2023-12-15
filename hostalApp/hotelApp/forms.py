from django import forms
from hotelApp.models import Hotel   
from hotelApp.models import Habitacion
from hotelApp.models import Pasajero
from hotelApp.models import PasajeroHabitacion
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

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
        widgets = {
            "llegadaClient": DateTimePickerInput(),
            "salidaClient": DateTimePickerInput(options={"format": "YYYY-MM-DD HH:mm:ss"}),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

class PasajeroHabitacionForm(forms.ModelForm):
    class Meta:
        model = PasajeroHabitacion
        fields = '__all__'