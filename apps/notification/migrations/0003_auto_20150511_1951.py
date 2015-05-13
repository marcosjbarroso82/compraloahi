# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_confignotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment'), ('prox', 'Near Favorite'), ('cal', 'Calification')], max_length=20),
            preserve_default=True,
        ),
    ]
