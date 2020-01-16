from datetime import datetime

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class StationManager(models.Manager):
    def get_by_natural_key(self, longitude, latitude):
        return self.get(longitude=longitude, latitude=latitude)


class Station(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    max_bikes_quantity = models.IntegerField(default=0)

    objects = StationManager()

    class Meta:
        unique_together = [['longitude', 'latitude']]

    def natural_key(self):
        return self.longitude, self.latitude





class Bike(models.Model):

    MODEL = (
        ('model X', 'model X'),
        ('model Y', 'model Y'),
        ('model Z', 'model Z'),
    )

    bike_model = models.CharField(choices=MODEL, max_length=200)
    actual_station = models.ForeignKey(Station, on_delete=models.SET_NULL, related_name='bikes', null=True, blank=True)

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    def clean(self):
        actual_station = self.actual_station
        print('model')
        if actual_station is not None:
            print('model')
            self.latitude = self.actual_station.latitude
            self.longitude = self.actual_station.longitude






class HireTransaction(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, blank=False, null=True)
    start = models.DateTimeField(blank=False, null=False, default=datetime.now())
    end = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    starting_station = models.ForeignKey(Station, related_name='starting_station',on_delete= models.CASCADE, blank=True, null=True, editable=True)
    ending_station = models.ForeignKey(Station, on_delete=models.CASCADE, blank=True, null=True)

    def as_dict(self):
        return {
            "id": self.id,
            "bike": {"model": self.bike.bike_model},
            "start": self.start,
            "end": self.end,
            "price": self.price,
            "starting_station": {"name": self.starting_station.name,
                                 "longitude": self.starting_station.longitude,
                                 "latitude": self.starting_station.latitude},
            "ending_station": {"name": self.starting_station.name,
                                 "longitude": self.starting_station.longitude,
                                 "latitude": self.starting_station.latitude},
        }


@receiver(pre_save, sender=HireTransaction)
def update_hire_transaction(sender, instance, *args, **kwargs):
        instance.starting_station = instance.bike.actual_station
        bike = Bike.objects.get(id=instance.bike.id)
        if instance.ending_station is None:
            bike.actual_station = None
            bike.save()
        else:
            bike.actual_station = instance.ending_station
            bike.save()






