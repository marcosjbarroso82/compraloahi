# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CounterWhered',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('whered', models.CharField(unique=True, max_length=100)),
                ('counter', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('seller', models.BooleanField(default=False)),
                ('buyer', models.BooleanField(default=False)),
                ('android', models.BooleanField(default=False)),
                ('ios', models.BooleanField(default=False)),
            ],
        ),
    ]
