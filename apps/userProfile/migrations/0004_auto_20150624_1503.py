# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_auto_20150624_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='status',
            field=models.IntegerField(choices=[(0, 'deactivate'), (1, 'activate')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
            preserve_default=True,
        ),
    ]
