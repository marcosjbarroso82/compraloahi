# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0007_ad_agenda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='agenda',
        ),
    ]
