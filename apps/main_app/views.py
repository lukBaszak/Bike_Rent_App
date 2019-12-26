from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.main_app.forms import ExtendedUserCreationForm


def homepage(request):

    return render(request, 'main/homepage.html')


def register_request(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Registered username: {}".format(username))
            login(request, user)
            messages.info(request, "You have been successfully logged into an account")
            return redirect("main_app:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = ExtendedUserCreationForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})


def login_request(request):

    if request.metod == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)


def logout_request(request):
    logout(request)

    messages.info(request, "You have been successfully logouted")

    return redirect('main_app:homepage')