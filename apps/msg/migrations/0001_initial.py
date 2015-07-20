# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(verbose_name='subject', max_length=30)),
                ('body', models.TextField(verbose_name='body', blank=True)),
                ('sent_at', models.DateTimeField(verbose_name='sent at', auto_now_add=True)),
                ('read_at', models.DateTimeField(null=True, blank=True, verbose_name='read at')),
                ('replied_at', models.DateTimeField(null=True, blank=True, verbose_name='replied at')),
                ('sender_archived', models.BooleanField(default=False, verbose_name='archived by sender')),
                ('recipient_archived', models.BooleanField(default=False, verbose_name='archived by recipient')),
                ('sender_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='deleted by sender at')),
                ('recipient_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='deleted by recipient at')),
                ('moderation_status', models.CharField(choices=[('p', 'Pending'), ('a', 'Accepted'), ('r', 'Rejected')], default='p', max_length=1, verbose_name='status')),
                ('moderation_date', models.DateTimeField(null=True, blank=True, verbose_name='moderated at')),
                ('moderation_reason', models.CharField(verbose_name='rejection reason', blank=True, max_length=120)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True, blank=True)),
                ('parent', models.ForeignKey(to='msg.Msg', null=True, verbose_name='parent message', blank=True, related_name='msg_next_messages')),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='recipient', blank=True, related_name='msg_received_messages')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='sender', blank=True, related_name='msg_sent_messages')),
                ('thread', models.ForeignKey(to='msg.Msg', null=True, verbose_name='root message', blank=True, related_name='msg_child_messages')),
            ],
            options={
                'verbose_name': 'message',
                'ordering': ['-sent_at', '-id'],
                'verbose_name_plural': 'messages',
            },
            bases=(models.Model,),
        ),
    ]
