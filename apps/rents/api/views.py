from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser

from apps.rents.api.serializers import RentTransactionSerializer, BikeSerializer, StationSerializer
from apps.rents.models import Station, HireTransaction


class StationViewSet(generics.ListAPIView):
    queryset = Station.objects.all()
    model = Station
    serializer_class = StationSerializer


class RentTransactionList(generics.ListAPIView):
    queryset = HireTransaction.objects.all()
    model = HireTransaction
    serializer_class = RentTransactionSerializer

    def get_queryset(self):
        sort_by = self.request.query_params.get("sort_by", "start")
        reversed_sorting = self.request.query_params.get("reversed", '1')
        user = self.request.user


        if reversed_sorting == '1':
            return HireTransaction.objects.order_by(sort_by).filter(user=user)

        elif reversed_sorting == '-1':

            return HireTransaction.objects.order_by(sort_by).reverse().filter(user=user)


@api_view(['POST'])
def UpdateBikeInformation(request):
    if request.METHOD == 'POST':
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

