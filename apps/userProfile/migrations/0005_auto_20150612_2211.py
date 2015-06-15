# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_auto_20150523_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='title',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
