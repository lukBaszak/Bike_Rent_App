import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render

from apps.rents.models import Hire_Transaction, Station


def transaction_details_request(request, transaction_id):

    transaction = Hire_Transaction.objects.get(id=transaction_id)

    transaction_json_good = serializers.serialize('json', [transaction,], indent=2, use_natural_foreign_keys=True)

    if transaction.user.username == request.user.username:
        return render(request, 'main/users/transaction_details.html', {'transaction': transaction_json_good})
