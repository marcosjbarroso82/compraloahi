# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('rating', '0002_auto_20150511_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='ad',
        ),
        migrations.AddField(
            model_name='rating',
            name='transaction_id',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='transaction_type',
            field=models.ForeignKey(to='contenttypes.ContentType', default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='voted',
            field=models.ForeignKey(related_name='user_voted', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='voter',
            field=models.ForeignKey(related_name='user_voter', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
