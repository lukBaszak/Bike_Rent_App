from rest_framework import serializers

from apps.rents.models import Station


class StationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Station
        fields = ['id', 'name', 'latitude', 'longitude', 'max_bikes_quantity']