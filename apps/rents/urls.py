from django.urls import path, include

from apps.rents import views

app_name = 'rents'

urlpatterns = [
    path('<int:transaction_id>/', views.transaction_details_request),

]