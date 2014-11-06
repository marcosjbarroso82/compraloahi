# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adLocation', '0002_auto_20141106_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adlocation',
            name='administrative_area_level_1',
            field=models.CharField(null=True, blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='adlocation',
            name='administrative_area_level_2',
            field=models.CharField(null=True, blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='adlocation',
            name='country',
            field=models.CharField(null=True, blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='adlocation',
            name='locality',
            field=models.CharField(null=True, blank=True, max_length=40),
        ),
    ]
