# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20170318_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
