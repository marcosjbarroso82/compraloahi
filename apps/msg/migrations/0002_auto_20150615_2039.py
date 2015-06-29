# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='sent_at',
            field=models.DateTimeField(verbose_name='sent at', auto_created=True),
            preserve_default=True,
        ),
    ]
