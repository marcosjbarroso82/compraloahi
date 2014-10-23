# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_auto_20141023_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(default='2013-01-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='profile'),
            preserve_default=False,
        ),
    ]
