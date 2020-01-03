from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Station(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    max_bikes_quantity = models.IntegerField(default=0)




class Bike(models.Model):

    MODEL = (
        ('model X', 'model X'),
        ('model Y', 'model Y'),
        ('model Z', 'model Z'),
    )

    bike_model = models.CharField(choices=MODEL, max_length=200)
    actual_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='bikes', null=True, blank=True)

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




class Hire_Transaction(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, blank=False, null=True)
    start = models.DateTimeField(blank=False, null=False, default=datetime.now())
    end = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    starting_station = models.ForeignKey(Station, on_delete= models.CASCADE, blank=True, null=True, editable=False)


@receiver(pre_save, sender=Hire_Transaction)
def update_hire_transaction(sender, instance, *args, **kwargs):
        instance.starting_station = instance.bike.actual_station
        bike = Bike.objects.get(id=instance.bike.id)
        bike.actual_station = None
        bike.save()






