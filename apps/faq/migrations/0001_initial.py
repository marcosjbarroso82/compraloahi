# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.TextField(help_text='The actual question itself.', verbose_name='question')),
                ('answer', models.TextField(help_text='The answer text.', blank=True, verbose_name='answer')),
                ('slug', models.SlugField(unique=True, verbose_name='slug', max_length=100)),
                ('status', models.IntegerField(default=0, verbose_name='status', choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Group Header')], help_text="Only questions with their status set to 'Active' will be displayed. Questions marked as 'Group Header' are treated as such by views and templates that are set up to use them.")),
                ('protected', models.BooleanField(default=False, verbose_name='is protected', help_text='Set true if this question is only visible by authenticated users.')),
                ('sort_order', models.IntegerField(default=0, verbose_name='sort order', help_text='The order you would like the question to be displayed.')),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('nr_views', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, related_name='+', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Frequently asked questions',
                'verbose_name': 'Frequent asked question',
                'ordering': ['sort_order', 'nr_views', 'created_on'],
            },
        ),
        migrations.CreateModel(
            name='QuestionScore',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('score', models.IntegerField(default=1, verbose_name='score', choices=[(0, 'No'), (1, 'Yes')])),
                ('ip_address', models.GenericIPAddressField(null=True, blank=True, verbose_name='IP address')),
                ('question', models.ForeignKey(to='faq.Question')),
                ('user', models.ForeignKey(default=-1, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=150)),
                ('slug', models.SlugField(verbose_name='slug', max_length=150)),
                ('sort_order', models.IntegerField(default=0, verbose_name='sort order', help_text='The order you would like the topic to be displayed.')),
                ('nr_views', models.IntegerField(default=0)),
                ('icon', models.ImageField(null=True, upload_to='topic_icons/', blank=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('description', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, related_name='+', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
                ('updated_by', models.ForeignKey(blank=True, related_name='+', null=True, verbose_name='updated by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Topics',
                'verbose_name': 'Topic',
                'ordering': ['sort_order', 'nr_views', 'name'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(verbose_name='topic', related_name='questions', to='faq.Topic'),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_by',
            field=models.ForeignKey(blank=True, related_name='+', null=True, verbose_name='updated by', to=settings.AUTH_USER_MODEL),
        ),
    ]
