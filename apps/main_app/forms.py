from absl.flags import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


class ExtendedUserCreationForm(UserCreationForm):

    email = forms.EmailField(required= True, )
    phone_number = PhoneNumberField(label='phone_number')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super(ExtendedUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("Phone number already exists")
        return phone_number

