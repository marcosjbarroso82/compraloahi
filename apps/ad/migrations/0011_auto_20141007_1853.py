# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0010_auto_20141007_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
