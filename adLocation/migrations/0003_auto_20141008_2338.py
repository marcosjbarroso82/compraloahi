# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adLocation', '0002_auto_20141008_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adlocation',
            name='ad',
            field=models.ForeignKey(to='ad.Ad', unique=True, related_name='locations'),
        ),
    ]
