# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0011_auto_20141007_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='agenda',
            field=models.ForeignKey(null=True, unique=True, to='agenda.Agenda', on_delete=django.db.models.deletion.SET_NULL, blank=True),
        ),
    ]
