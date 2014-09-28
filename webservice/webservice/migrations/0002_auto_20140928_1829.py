# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def populate_initial_data(apps, schema_editor):
    BalanceSheetAccount = apps.get_model("webservice", "BalanceSheetAccount")
    account = BalanceSheetAccount(name="Test Account", code="AT34123412341234", description="A test account.",
                                  is_container=False, is_root=True)
    account.save()


class Migration(migrations.Migration):
    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_initial_data),
    ]