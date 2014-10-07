# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_auto_20141007_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='friday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='agenda.Day', related_name='friday'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='monday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='agenda.Day', related_name='monday'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='saturday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='agenda.Day', related_name='saturday'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='sunday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='agenda.Day', related_name='sunday'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='thursday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='agenda.Day', related_name='thursday'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='tuesday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='agenda.Day', related_name='tuesday'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='wednesday',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='agenda.Day', related_name='wednesday'),
        ),
    ]
