from webservice.models import BalanceSheetAccount
from rest_framework import serializers


class BalanceSheetAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceSheetAccount
        fields = ('id', 'code', 'created', 'description', 'is_container', 'is_root', 'name', 'notes')
