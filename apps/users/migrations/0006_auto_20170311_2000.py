# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170311_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='approval_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='approved_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to='users.Teacher'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='assigned_approver',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_approver', to='users.Teacher'),
        ),
    ]
