# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adLocation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adlocation',
            name='administrative_area_level_1',
            field=models.CharField(max_length=40, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adlocation',
            name='administrative_area_level_2',
            field=models.CharField(max_length=40, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adlocation',
            name='country',
            field=models.CharField(max_length=40, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adlocation',
            name='locality',
            field=models.CharField(max_length=40, default=''),
            preserve_default=False,
        ),
    ]
