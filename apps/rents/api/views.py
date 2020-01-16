from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser

from apps.api.serializers import StationSerializer
from apps.rents.api.serializers import RentTransactionSerializer
from apps.rents.models import Station, HireTransaction


class StationView(generics.ListAPIView):
    queryset = Station.objects.all()
    model = Station
    serializer_class = StationSerializer


class RentTransactionList(generics.ListAPIView):
    queryset = HireTransaction.objects.all()
    model = HireTransaction
    serializer_class = RentTransactionSerializer

    def get_queryset(self):
        sort_by = self.request.query_params.get("sort_by", None)
        reversed_sorting = self.request.query_params.get("reversed", None)
        user = self.request.user

        if reversed_sorting == '1':
            print('1')
            return HireTransaction.objects.order_by().order_by(sort_by).filter(user=user)

        elif reversed_sorting == '-1':
            print('-1')
            return HireTransaction.objects.order_by().order_by(sort_by).reverse().filter(user=user)


