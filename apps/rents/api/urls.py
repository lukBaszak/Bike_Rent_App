from django.urls import path, include
from rest_framework import routers

from apps.rents.api import views



urlpatterns = [
    path('', views.RentTransactionList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('update_bike/', views.UpdateBikeInformation)
]