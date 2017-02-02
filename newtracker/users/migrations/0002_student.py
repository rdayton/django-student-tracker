# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 01:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('major', models.CharField(blank=True, max_length=30, null=True)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('grade_level', models.IntegerField()),
            ],
        ),
    ]