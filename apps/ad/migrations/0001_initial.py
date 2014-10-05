# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.ad.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('published', models.BooleanField(default=True)),
                ('tags_temp2', apps.ad.models.TagField(default=[])),
            ],
            options={
                'verbose_name_plural': 'Ads',
                'verbose_name': 'Ad',
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='ad')),
                ('ad_id', models.ForeignKey(to='ad.Ad', related_name='images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
