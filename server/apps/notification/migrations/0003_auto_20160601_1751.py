# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20160601_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
