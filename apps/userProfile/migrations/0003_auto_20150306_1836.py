# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_auto_20150123_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='type',
            field=models.CharField(max_length=200, choices=[('TEL', 'Telefono'), ('CEL', 'Celular'), ('FAX', 'Fax')]),
        ),
    ]
