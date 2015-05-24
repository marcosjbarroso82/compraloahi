# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_auto_20150523_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='column',
            field=models.PositiveIntegerField(default=4, choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
            preserve_default=True,
        ),
    ]
