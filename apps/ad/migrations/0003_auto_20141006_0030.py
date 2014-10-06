# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_adimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimage',
            name='image',
            field=models.ImageField(upload_to='ad'),
        ),
    ]
