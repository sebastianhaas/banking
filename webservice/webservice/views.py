from django.shortcuts import render
from webservice.models import BalanceSheetAccount
from webservice.serializers import BalanceSheetAccountSerializer
from rest_framework import generics

# Create your views here.


class BalanceSheetAccountList(generics.ListAPIView):
    queryset = BalanceSheetAccount.objects.all()
    serializer_class = BalanceSheetAccountSerializer