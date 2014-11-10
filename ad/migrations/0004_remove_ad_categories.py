# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_auto_20141106_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='categories',
        ),
    ]
