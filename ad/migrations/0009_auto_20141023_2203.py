# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0008_auto_20141022_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='categories',
            field=taggit.managers.TaggableManager(through='ad.CategoryTaggedItem', verbose_name='categories', to='ad.CategoryTag', blank=True, help_text='A comma-separated list of tags.'),
        ),
    ]
