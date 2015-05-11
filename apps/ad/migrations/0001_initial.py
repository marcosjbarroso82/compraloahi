# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('published', models.BooleanField(default=True)),
                ('short_description', models.CharField(max_length=100)),
                ('price', models.DecimalField(default='0.00', max_digits=10, decimal_places=2)),
                ('author', models.ForeignKey(related_name='ads', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ads',
                'ordering': ['-created'],
                'verbose_name': 'Ad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to='ad')),
                ('ad_id', models.ForeignKey(related_name='images', to='ad.Ad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ad',
            name='categories',
            field=models.ManyToManyField(to='ad.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', blank=True, verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem'),
            preserve_default=True,
        ),
    ]
