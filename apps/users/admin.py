from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from apps.rents.models import Station
from apps.users.models import Profile



admin.site.register(Profile)


