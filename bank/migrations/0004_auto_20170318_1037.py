# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20170318_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bank',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='bank.Bank'),
        ),
    ]
