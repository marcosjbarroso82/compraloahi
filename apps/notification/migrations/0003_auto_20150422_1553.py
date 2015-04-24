# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20150422_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': 'Ads', 'verbose_name': 'Ad', 'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='notification',
            name='extras',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
