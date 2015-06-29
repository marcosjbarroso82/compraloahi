# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0002_auto_20150615_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='sent_at',
            field=models.DateTimeField(verbose_name='sent at', auto_now_add=True),
            preserve_default=True,
        ),
    ]
