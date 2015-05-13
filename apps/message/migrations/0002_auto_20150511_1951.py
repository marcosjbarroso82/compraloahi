# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagechannel',
            name='status',
            field=models.CharField(default='act', max_length=20, choices=[('des', 'desactivated'), ('pen', 'pending'), ('ter', 'terminated'), ('exp', 'expired'), ('appr', 'approved'), ('rej', 'rejected')]),
            preserve_default=True,
        ),
    ]
