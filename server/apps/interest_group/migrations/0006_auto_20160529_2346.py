# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_group', '0005_auto_20160529_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='interestgroup',
            name='status',
            field=models.IntegerField(choices=[(0, 'Active'), (1, 'Delete')], default=0),
        ),
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.IntegerField(choices=[(0, 'Admin'), (1, 'Member')], default=1),
        ),
    ]
