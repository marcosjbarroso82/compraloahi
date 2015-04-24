# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(max_length=20, choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment')]),
            preserve_default=True,
        ),
    ]
