from rest_framework import serializers

from apps.rents.models import Station, HireTransaction, Bike


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ['id', 'name', 'latitude', 'longitude', 'max_bikes_quantity']


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['bike_model']


class RentTransactionSerializer(serializers.ModelSerializer):

    bike = BikeSerializer()

    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = HireTransaction
        fields = ['bike', 'start', 'end', 'price', 'starting_station', 'ending_station']


