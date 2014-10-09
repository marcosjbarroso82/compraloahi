# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_auto_20141006_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=40)),
                ('ad', models.ForeignKey(to='ad.Ad', related_name='locations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
