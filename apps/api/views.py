from rest_framework import viewsets, generics

from apps.api.serializers import StationSerializer
from apps.rents.models import Station


class StationView(generics.ListAPIView):
    queryset = Station.objects.all()
    model = Station
    serializer_class = StationSerializer
