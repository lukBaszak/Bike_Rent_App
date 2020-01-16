from django.urls import path, include

from apps.users import views
from apps.rents import views as rents_views

app_name = 'users'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("register/", views.register_request, name='register_request'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('account/', views.my_account, name='my_account'),
    path('history/', views.history, name='history'),
    path('details/<int:transaction_id>/', rents_views.transaction_details_request),

    path('api/v1/transactions/', include('apps.rents.api.urls')),
    path('api/v1/users/', include('apps.users.api.urls')),
]