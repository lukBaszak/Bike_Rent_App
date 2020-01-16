from django.contrib import admin

from BikeRentalApp import settings
from apps.rents.forms import BikeForm
from apps.rents.models import Bike, HireTransaction, Station

from django import forms



class BikeAdmin(admin.ModelAdmin):
    form = BikeForm


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_bikes_quantity','latitude', 'longitude', )
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name','max_bikes_quantity', 'latitude', 'longitude', )
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'location_picker.js',
            )



admin.site.register(Bike, BikeAdmin)
admin.site.register(HireTransaction)



