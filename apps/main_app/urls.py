from django.urls import path

from apps.main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("register/", views.register_request, name='register_request'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout_request')
]