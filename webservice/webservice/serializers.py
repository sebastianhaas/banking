from webservice.models import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'code', 'created', 'description', 'is_container', 'is_root', 'name', 'notes')
