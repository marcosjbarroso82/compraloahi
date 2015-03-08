# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_auto_20141113_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='short_description',
            field=models.CharField(max_length=100),
        ),
    ]
