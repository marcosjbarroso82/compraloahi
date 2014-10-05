# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import apps.ad.models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='tags_temp2',
        ),
        migrations.AddField(
            model_name='ad',
            name='tags_temp6',
            field=apps.ad.models.TagField(default=datetime.date(2014, 10, 5)),
            preserve_default=False,
        ),
    ]
