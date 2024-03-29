from django.db import models

# Create your models here.


class BasicModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User')

    class Meta:
        abstract = True


class Tag(BasicModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name


class Account(BasicModel):
    # Balance Sheet Accounts
    # - Assets
    BANK_ACCOUNT = 0
    CASH_ACCOUNT = 1
    OTHER_ASSETS = 2

    # - Liabilities
    CREDIT_CARD = 3
    OTHER_LIABILITIES = 4

    # - Equity
    EQUITY = 5

    # Nominal Accounts
    # - Income
    INCOME = 6

     # - Expenses
    EXPENSES = 7

    ACCOUNT_TYPES = (
        (BANK_ACCOUNT, 'Bank account'),
        (CASH_ACCOUNT, 'Cash account'),
        (OTHER_ASSETS, 'Other assets'),
        (CREDIT_CARD, 'Credit card'),
        (OTHER_LIABILITIES, 'Other liabilities'),
        (EQUITY, 'Equity'),
        (INCOME, 'Income'),
        (EXPENSES, 'Expenses'),
    )

    code = models.CharField(max_length=50)
    description = models.TextField()
    is_container = models.BooleanField(default=False)
    is_root = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    notes = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True)
    tag = models.ManyToManyField('Tag')
    type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPES)

    def __str__(self):
        return '%s [%s]' % (self.name, self.code)


class Transaction(BasicModel):
    date = models.DateField()
    number = models.CharField(max_length=50)
    tag = models.ManyToManyField('Tag')
    text = models.CharField(max_length=200)
    time = models.TimeField(blank=True, null=True)

    def has_time(self):
        return self.time is not None


class Split(BasicModel):
    CLEARED = 'c'
    NEW = 'n'
    RECONCILED = 'r'
    RECONCILIATION_STATE_CHOICES = (
        (NEW, 'New'),
        (CLEARED, 'Cleared'),
        (RECONCILED, 'Reconciled'),
    )
    account = models.ForeignKey('Account')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    reconciliation_state = models.CharField(max_length=1,
                                            choices=RECONCILIATION_STATE_CHOICES,
                                            default=NEW)
    text = models.CharField(max_length=200)
    transaction = models.ForeignKey('Transaction')

    def is_reconciled(self):
        return self.reconciliation_state is Split.RECONCILED


class Device(BasicModel):
    brand = models.CharField(max_length=100)
    build_id = models.CharField(max_length=100)
    description = models.TextField()
    last_active = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    serial = models.CharField(max_length=100)
    tag = models.ManyToManyField('Tag')


class InvoiceScan(BasicModel):
    image = models.ImageField()


class Location(BasicModel):
    accuracy = models.FloatField(default=-1)
    altitude = models.FloatField(default=-1)
    bearing = models.FloatField(default=-1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField(default=-1)