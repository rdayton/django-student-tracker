# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170312_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitystatus',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]