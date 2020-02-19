from django.conf.urls import url
from django.contrib.auth.models import User
from django.urls import path

from apps.users.api import views



urlpatterns = [
    path('profile_information/', views.profile_detail)
]