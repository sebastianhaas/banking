from webservice.models import BalanceSheetAccount, NominalAccount, EquityAccount, ImbalanceAccount
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'code', 'created', 'description', 'is_container', 'is_root', 'name', 'notes')


class BalanceSheetAccountSerializer(AccountSerializer):
    class Meta:
        model = BalanceSheetAccount


class NominalAccountSerializer(AccountSerializer):
    class Meta:
        model = NominalAccount


class EquityAccountSerializer(AccountSerializer):
    class Meta:
        model = EquityAccount


class ImbalanceAccountSerializer(AccountSerializer):
    class Meta:
        model = ImbalanceAccount