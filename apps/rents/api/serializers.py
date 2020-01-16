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
    starting_station = StationSerializer()
    ending_station = StationSerializer()

    class Meta:
        model = HireTransaction
        fields = ['id','bike', 'start', 'end', 'price', 'starting_station', 'ending_station']


