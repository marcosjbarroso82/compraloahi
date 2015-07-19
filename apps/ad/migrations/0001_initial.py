# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(unique_with=('pub_date',), populate_from='title', editable=False)),
                ('published', models.BooleanField(default=True)),
                ('short_description', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=10, default='0.00', decimal_places=2)),
                ('store_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='ads')),
            ],
            options={
                'verbose_name': 'Ad',
                'ordering': ['-created'],
                'verbose_name_plural': 'Ads',
            },
        ),
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='ad')),
                ('default', models.BooleanField(default=False)),
                ('ad_id', models.ForeignKey(to='ad.Ad', related_name='images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='categories',
            field=models.ManyToManyField(to='ad.Category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag', blank=True),
        ),
    ]
