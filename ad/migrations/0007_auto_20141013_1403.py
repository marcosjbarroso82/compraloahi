# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_auto_20141006_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags'),
        ),
    ]