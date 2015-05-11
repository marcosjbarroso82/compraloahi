# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageChannel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(auto_created=True, null=True)),
                ('status', models.CharField(choices=[('des', 'desactivated'), ('act', 'activated'), ('exp', 'expired')], default='des', max_length=20)),
                ('ad', models.ForeignKey(to='ad.Ad')),
                ('recipient', models.ForeignKey(related_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
