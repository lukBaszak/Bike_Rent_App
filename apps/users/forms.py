from absl.flags import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

from apps.users.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date', 'phone_number')




