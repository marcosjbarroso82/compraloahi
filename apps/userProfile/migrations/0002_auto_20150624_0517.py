# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='style',
            field=django_pgjson.fields.JsonField(default={'font_color': '#00000', 'column': 4, 'background_color': '#f2f2f2'}),
            preserve_default=True,
        ),
    ]
