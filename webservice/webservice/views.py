from webservice.models import Account
from webservice.serializers import AccountSerializer
from rest_framework import generics

# Create your views here.


class AccountList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer