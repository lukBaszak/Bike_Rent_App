from django.contrib.auth.models import User
from django.db import models

class Bike(models.Model):
    bike_model = models.CharField(default='the new one', max_length=200)


class Hire_Transaction(models.Model):

    user = models.ManyToManyField(User)
    bike = models.ManyToManyField(Bike)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)





