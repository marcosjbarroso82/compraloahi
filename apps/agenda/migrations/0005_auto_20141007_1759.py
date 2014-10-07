# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_remove_agenda_monday'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='friday',
            field=models.ForeignKey(null=True, to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, related_name='friday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='monday',
            field=models.ForeignKey(null=True, to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, related_name='monday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='saturday',
            field=models.ForeignKey(null=True, to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, related_name='saturday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='sunday',
            field=models.ForeignKey(null=True, to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, related_name='sunday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='thursday',
            field=models.ForeignKey(null=True, to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, related_name='thursday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='tuesday',
            field=models.ForeignKey(null=True, to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, related_name='tuesday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='wednesday',
            field=models.ForeignKey(null=True, to='agenda.Day', on_delete=django.db.models.deletion.SET_NULL, related_name='wednesday'),
            preserve_default=True,
        ),
    ]
