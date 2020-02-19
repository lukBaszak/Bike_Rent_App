
from rest_framework import serializers
from apps.users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = ['id', 'bio', 'birth_date', 'qr_identifier', 'balance']
