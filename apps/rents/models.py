from datetime import datetime

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.payments.models import PaymentTransaction


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

    def __str__(self):
        return str(self.id) + self.name



class Bike(models.Model):
    MODEL = (
        ('model X', 'model X'),
        ('model Y', 'model Y'),
        ('model Z', 'model Z'),
    )

    STATUS = (
        ('FREE', 'FREE'),
        ('TAKEN', 'TAKEN'),
        ('BROKEN', 'BROKEN')
    )

    bike_model = models.CharField(choices=MODEL, max_length=200)
    status = models.CharField(choices=STATUS, default='FREE', max_length=30)
    actual_station = models.ForeignKey(Station, on_delete=models.SET_NULL, related_name='bikes', null=True, blank=True)

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)


    def clean(self):
        actual_station = self.actual_station
        if actual_station is not None:
            self.latitude = self.actual_station.latitude
            self.longitude = self.actual_station.longitude

    def __str__(self):
        return "id:" + str(self.id) + " " + self.bike_model



class HireTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, blank=False, null=True)
    start = models.DateTimeField(blank=False, null=False, default=datetime.now())
    end = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)
    starting_station = models.ForeignKey(Station, related_name='starting_station', on_delete=models.CASCADE, blank=True,
                                         null=True, editable=True)
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

    def __str__(self):
        return self.user.username + " " + str(self.start)




@receiver(post_save, sender=HireTransaction)
def update_bike_status(sender, instance, created, **kwargs):
    if created:
        bike = Bike.objects.get(id=instance.bike.id)
        bike.status = 'TAKEN'
        bike.save()


@receiver(post_save, sender=Bike)
def update_bike_status(sender, instance, created, **kwargs):

    # TODO check if changed value Taken -> Free signaler

    if True:
        hire_transaction = HireTransaction.objects.get(bike=instance, end__isnull=True)
        hire_transaction.end = datetime.now()
        hire_transaction.ending_station = instance.actual_station

        hire_transaction.price = (hire_transaction.start.timestamp() * 1000 - hire_transaction.end.timestamp() * 1000) / 60000 * 0.5
        hire_transaction.save()


@receiver(post_save, sender=HireTransaction)
def updated_hire_transaction_status(sender, instance, created, **kwargs):
    if instance.end is not None:
        PaymentTransaction.objects.create(hire_transaction=instance, price=instance.price)
