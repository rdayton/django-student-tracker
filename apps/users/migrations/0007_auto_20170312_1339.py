# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 17:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170311_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2017, 3, 12, 13, 39, 25, 583327))),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='approval_date',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='approved_by',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='assigned_approver',
        ),
        migrations.RemoveField(
            model_name='student',
            name='activities',
        ),
        migrations.AddField(
            model_name='activitystatus',
            name='activity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Activity'),
        ),
        migrations.AddField(
            model_name='activitystatus',
            name='approved_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to='users.Teacher'),
        ),
        migrations.AddField(
            model_name='activitystatus',
            name='assigned_approver',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_approver', to='users.Teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='activity_statuses',
            field=models.ManyToManyField(blank=True, to='users.ActivityStatus'),
        ),
    ]
