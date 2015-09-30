# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField(help_text='The actual question itself.', verbose_name='question')),
                ('answer', models.TextField(help_text='The answer text.', verbose_name='answer', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
                ('status', models.IntegerField(verbose_name='status', help_text="Only questions with their status set to 'Active' will be displayed. Questions marked as 'Group Header' are treated as such by views and templates that are set up to use them.", choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Group Header')], default=0)),
                ('protected', models.BooleanField(help_text='Set true if this question is only visible by authenticated users.', verbose_name='is protected', default=False)),
                ('sort_order', models.IntegerField(help_text='The order you would like the question to be displayed.', verbose_name='sort order', default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('nr_views', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', verbose_name='created by')),
            ],
            options={
                'ordering': ['sort_order', 'nr_views', 'created_on'],
                'verbose_name': 'Frequent asked question',
                'verbose_name_plural': 'Frequently asked questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionScore',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='score', choices=[(0, 'No'), (1, 'Yes')], default=1)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP address', blank=True)),
                ('question', models.ForeignKey(to='faq.Question')),
                ('user', models.ForeignKey(blank=True, null=True, default=-1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('slug', models.SlugField(max_length=150, verbose_name='slug')),
                ('sort_order', models.IntegerField(help_text='The order you would like the topic to be displayed.', verbose_name='sort order', default=0)),
                ('nr_views', models.IntegerField(default=0)),
                ('icon', models.ImageField(null=True, upload_to='topic_icons/', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('created_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', verbose_name='created by')),
                ('site', models.ForeignKey(blank=True, null=True, to='sites.Site')),
                ('updated_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', verbose_name='updated by')),
            ],
            options={
                'ordering': ['sort_order', 'nr_views', 'name'],
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(verbose_name='topic', to='faq.Topic', related_name='questions'),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='+', verbose_name='updated by'),
        ),
    ]
