# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 17:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170312_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitystatus',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 12, 17, 46, 37, 375811, tzinfo=utc)),
        ),
    ]
