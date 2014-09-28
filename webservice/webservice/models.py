from django.db import models

# Create your models here.


class Account(models.Model):
    code = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    is_container = models.BooleanField(default=False)
    is_root = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    notes = models.TextField()

    class Meta:
        abstract = True


class BalanceSheetAccount(Account):
    pass


class NominalAccount(Account):
    pass


class EquityAccount(BalanceSheetAccount):
    pass


class ImbalanceAccount(BalanceSheetAccount):
    pass