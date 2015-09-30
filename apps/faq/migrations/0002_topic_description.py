# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.CharField(default='descripcion', max_length=255),
            preserve_default=False,
        ),
    ]
