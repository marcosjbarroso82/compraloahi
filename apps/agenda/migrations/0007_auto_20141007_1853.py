# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_auto_20141007_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='wednesday',
        ),
    ]
