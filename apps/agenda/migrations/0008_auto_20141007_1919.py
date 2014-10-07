# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_auto_20141007_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='friday',
            field=models.ForeignKey(null=True, related_name='friday', to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='saturday',
            field=models.ForeignKey(null=True, related_name='saturday', to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='sunday',
            field=models.ForeignKey(null=True, related_name='sunday', to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='thursday',
            field=models.ForeignKey(null=True, related_name='thursday', to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='wednesday',
            field=models.ForeignKey(null=True, related_name='wednesday', to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day',
            name='time_begin',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='day',
            name='time_end',
            field=models.TimeField(default='23:59:59'),
        ),
    ]
