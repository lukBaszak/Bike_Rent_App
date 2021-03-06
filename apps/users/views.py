from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from numpy import shape
import pyqrcode
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from apps.users.forms import UserCreationForm, ExtendedUserForm, ProfileForm
from apps.rents.models import Station, Bike, HireTransaction
import json

from apps.users.models import Profile


def homepage(request):

    stations = Station.objects.values_list('name', 'longitude', 'latitude', 'max_bikes_quantity')
    stations_json = json.dumps(list(stations), cls=DjangoJSONEncoder)

    bikes = Bike.objects.values_list('bike_model','longitude', 'latitude')
    bikes_json = json.dumps(list(bikes), cls=DjangoJSONEncoder)

    return render(request, 'main/users/homepage.html', context={'stations': stations_json,
                                                          'bikes': bikes_json})

def history(request):
    if request.user.is_authenticated:
        hire_transactions = request.user.hiretransaction_set.all()
        transactions_dict = [transaction.as_dict() for transaction in hire_transactions]
        transactions_json = json.dumps(list(transactions_dict), cls=DjangoJSONEncoder)
        return render(request, 'main/users/history.html')


def register_request(request):
    if request.method == "POST":
        form = ExtendedUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Registered username: {}".format(username))
            login(request, user)
            messages.info(request, "You have been successfully logged into an account")
            return render(request, 'main/users/homepage.html')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request=request,
                          template_name="main/users/register.html",
                          context={"form": form})

    form = ExtendedUserForm
    return render(request=request,
                  template_name="main/users/register.html",
                  context={"form": form})


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')

                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/users/login.html",
                  context={"form": form})


def logout_request(request):
    logout(request)

    messages.info(request, "You have been successfully logouted")

    return redirect('users:homepage')



def my_account(request):

    user_profile = ProfileForm(instance=request.user.profile)

    hire_transactions = request.user.hiretransaction_set.all().order_by('-id')[:5]
    transactions_dict = [transaction.as_dict() for transaction in hire_transactions]
    transactions_json = json.dumps(list(transactions_dict), cls=DjangoJSONEncoder)
    return render(request, 'main/users/my_account.html', { "profile": user_profile,
                                                        "transactions": transactions_json})




