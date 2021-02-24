# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 01:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('active_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
