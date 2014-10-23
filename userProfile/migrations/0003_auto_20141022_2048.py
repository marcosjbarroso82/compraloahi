# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_userlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=50, default='adasd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=50, default='asdasd'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userlocation',
            name='userProfile',
            field=models.ForeignKey(to='userProfile.UserProfile', related_name='locations'),
        ),
    ]
