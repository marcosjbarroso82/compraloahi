# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
            },
            bases=(models.Model,),
        ),
    ]
