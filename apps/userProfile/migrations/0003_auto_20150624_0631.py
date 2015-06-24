# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields
import autoslug.fields
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_auto_20150624_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False, default=datetime.datetime(2015, 6, 24, 6, 31, 52, 580043, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='style',
            field=django_pgjson.fields.JsonField(default={'font_color': '#00000', 'column': 4, 'background_color': '#f9f9f9'}),
            preserve_default=True,
        ),
    ]
