# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20141007_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='monday',
        ),
    ]
