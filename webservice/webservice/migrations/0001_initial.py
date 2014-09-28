# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSheetAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('is_container', models.BooleanField(default=False)),
                ('is_root', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EquityAccount',
            fields=[
                ('balancesheetaccount_ptr', models.OneToOneField(auto_created=True, to='webservice.BalanceSheetAccount', primary_key=True, parent_link=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('webservice.balancesheetaccount',),
        ),
        migrations.CreateModel(
            name='ImbalanceAccount',
            fields=[
                ('balancesheetaccount_ptr', models.OneToOneField(auto_created=True, to='webservice.BalanceSheetAccount', primary_key=True, parent_link=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('webservice.balancesheetaccount',),
        ),
        migrations.CreateModel(
            name='NominalAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('is_container', models.BooleanField(default=False)),
                ('is_root', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
