# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
        ('ad', '0006_auto_20141006_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='agenda',
            field=models.OneToOneField(to='agenda.Agenda', null=True),
            preserve_default=True,
        ),
    ]
