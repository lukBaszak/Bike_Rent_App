
from django import forms

from apps.rents.models import Hire_Transaction, Bike



class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ('bike_model', 'actual_station', 'latitude', 'longitude')

    def clean(self):
        actual_station = self.cleaned_data.get('actual_station')
        print('lwfedwefwefwefwefwefwe')
        if actual_station is not None:
            print('hello')
            self.latitude = actual_station.latitude
            self.longitude = actual_station.longitude

        return self.cleaned_data


