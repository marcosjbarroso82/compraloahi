# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_ad_store_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 22, 11, 22, 266870, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
