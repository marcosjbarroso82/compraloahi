# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('ad', '0007_auto_20141013_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100, unique=True)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(verbose_name='Content type', to='contenttypes.ContentType', related_name='ad_categorytaggeditem_tagged_items')),
                ('tag', models.ForeignKey(to='ad.CategoryTag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ad',
            name='categories',
            field=taggit.managers.TaggableManager(verbose_name='categories', help_text='A comma-separated list of tags.', to='ad.CategoryTag', blank=True, through='ad.CategoryTaggedItem'),
            preserve_default=True,
        ),
    ]
