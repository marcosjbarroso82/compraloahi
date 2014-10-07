# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_remove_agenda_monday'),
        ('ad', '0008_remove_ad_agenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='agenda',
            field=models.ForeignKey(null=True, unique=True, to='agenda.Agenda'),
            preserve_default=True,
        ),
    ]
