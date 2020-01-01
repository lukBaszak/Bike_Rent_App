from django.urls import path

from apps.users import views

app_name = 'users'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("register/", views.register_request, name='register_request'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('account/', views.my_account, name='my_account')
]