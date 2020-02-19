"""BikeRentalApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.rents.api.views import StationViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.rents.urls')),
    path('', include('apps.users.urls')),
    path('stations/', StationViewSet.as_view()),

    path('api/v1/transactions/', include('apps.rents.api.urls')),
    path('api/v1/users/', include('apps.users.api.urls')),

]
