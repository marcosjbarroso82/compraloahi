# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageChannel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateField(null=True, auto_created=True)),
                ('status', models.CharField(choices=[('des', 'desactivated'), ('pen', 'pending'), ('ter', 'terminated'), ('exp', 'expired'), ('appr', 'approved'), ('rej', 'rejected')], default='act', max_length=20)),
                ('ad', models.ForeignKey(to='ad.Ad')),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='recipient')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
