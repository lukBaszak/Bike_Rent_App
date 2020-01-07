from absl.flags import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django_registration.forms import RegistrationFormUniqueEmail
from phonenumber_field.formfields import PhoneNumberField

from apps.users.models import Profile


class ExtendedUserForm(RegistrationFormUniqueEmail):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(ExtendedUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date', 'phone_number')




