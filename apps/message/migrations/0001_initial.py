# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad', '0006_auto_20141113_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(auto_created=True, null=True)),
                ('status', models.CharField(choices=[('des', 'desactivated'), ('act', 'activated'), ('exp', 'expired')], default='des', max_length=20)),
                ('ad', models.ForeignKey(to='apps.ad.Ad')),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='recipient')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
