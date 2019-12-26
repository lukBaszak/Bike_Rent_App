from django.contrib import admin

from apps.rental_app.models import Bike, Hire_Transaction

admin.site.register(Bike)
admin.site.register(Hire_Transaction)