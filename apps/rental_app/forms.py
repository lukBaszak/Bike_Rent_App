
from django import forms

from apps.rental_app.models import Hire_Transaction


class TransactionForm(forms.Form):

    price = forms.FloatField(null=True, blank=True)

    class Meta:
        model = Hire_Transaction
        fields = ('user', 'bike', 'start', 'end', 'price')

