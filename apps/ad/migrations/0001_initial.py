# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('pub_date',))),
                ('published', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=1, choices=[('1', 'Active'), ('0', 'Delete')])),
                ('short_description', models.CharField(max_length=100)),
                ('price', models.DecimalField(default='0.00', max_digits=10, decimal_places=2)),
                ('store_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='ads')),
            ],
            options={
                'verbose_name_plural': 'Ads',
                'verbose_name': 'Ad',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to='ad')),
                ('default', models.BooleanField(default=False)),
                ('ad_id', models.ForeignKey(to='ad.Ad', related_name='images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', blank=True, to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem'),
        ),
    ]
