# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_auto_20170318_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankaccount',
            options={'verbose_name_plural': 'Bank Accounts'},
        ),
        migrations.AlterModelOptions(
            name='bankbranch',
            options={'verbose_name_plural': 'Bank Branches'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.BankBranch'),
        ),
    ]
