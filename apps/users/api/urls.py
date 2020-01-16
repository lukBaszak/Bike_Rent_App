from django.contrib.auth.models import User

from apps.api import serializers
from apps.rents.models import HireTransaction


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=HireTransaction.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
