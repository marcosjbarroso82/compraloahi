# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.FloatField(default='0.00'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='short_description',
            field=models.CharField(max_length=120, default='Descripcion corta...'),
            preserve_default=False,
        ),
    ]
