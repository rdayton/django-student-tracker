# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 22:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170304_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='approval_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='approved_by',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to='users.Teacher'),
        ),
        migrations.AddField(
            model_name='activity',
            name='assigned_approver',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_approver', to='users.Teacher'),
        ),
    ]