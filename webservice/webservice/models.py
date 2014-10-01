from django.db import models

# Create your models here.


class BasicModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User')

    class Meta:
        abstract = True


class Account(BasicModel):
    code = models.CharField(max_length=50)
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


class EquityAccount(Account):
    pass


class ImbalanceAccount(Account):
    pass


class Tag(BasicModel):
    name = models.CharField(max_length=50)


class Device(BasicModel):
    name = models.CharField(max_length=50)
    build_id = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)

