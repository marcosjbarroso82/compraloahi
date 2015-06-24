# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_auto_20150624_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='status',
            field=models.IntegerField(choices=[(0, 'deactivate'), (1, 'activate')], default=0),
            preserve_default=True,
        ),
    ]
