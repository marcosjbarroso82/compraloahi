# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('pub_date',))),
                ('published', models.BooleanField(default=True)),
                ('short_description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('store_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='ads', to=settings.AUTH_USER_MODEL)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='ad')),
                ('default', models.BooleanField(default=False)),
                ('ad_id', models.ForeignKey(related_name='images', to='ad.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
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
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', blank=True, to='taggit.Tag'),
        ),
    ]
