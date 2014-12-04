# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_auto_20141029_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
        ),
    ]
