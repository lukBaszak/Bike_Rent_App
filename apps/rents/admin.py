from django.contrib import admin

from BikeRentalApp import settings
from apps.rents.forms import BikeForm
from apps.rents.models import Bike, Hire_Transaction, Station

from django import forms



class BikeAdmin(admin.ModelAdmin):
    form = BikeForm





admin.site.register(Bike, BikeAdmin)
admin.site.register(Hire_Transaction)
admin.site.register(Station)


