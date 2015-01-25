# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlocation',
            name='radius',
            field=models.IntegerField(default=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phone',
            name='type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile/images.jpg', upload_to='profile'),
        ),
    ]
