# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('subject', models.CharField(max_length=30, verbose_name='subject')),
                ('body', models.TextField(blank=True, verbose_name='body')),
                ('sent_at', models.DateTimeField(verbose_name='sent at', auto_now_add=True)),
                ('read_at', models.DateTimeField(verbose_name='read at', blank=True, null=True)),
                ('replied_at', models.DateTimeField(verbose_name='replied at', blank=True, null=True)),
                ('sender_archived', models.BooleanField(default=False, verbose_name='archived by sender')),
                ('recipient_archived', models.BooleanField(default=False, verbose_name='archived by recipient')),
                ('sender_deleted_at', models.DateTimeField(verbose_name='deleted by sender at', blank=True, null=True)),
                ('recipient_deleted_at', models.DateTimeField(verbose_name='deleted by recipient at', blank=True, null=True)),
                ('moderation_status', models.CharField(choices=[('p', 'Pending'), ('a', 'Accepted'), ('r', 'Rejected')], max_length=1, default='p', verbose_name='status')),
                ('moderation_date', models.DateTimeField(verbose_name='moderated at', blank=True, null=True)),
                ('moderation_reason', models.CharField(max_length=120, blank=True, verbose_name='rejection reason')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', blank=True, null=True)),
                ('parent', models.ForeignKey(to='msg.Msg', null=True, blank=True, verbose_name='parent message', related_name='msg_next_messages')),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='recipient', related_name='msg_received_messages')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='sender', related_name='msg_sent_messages')),
                ('thread', models.ForeignKey(to='msg.Msg', null=True, blank=True, verbose_name='root message', related_name='msg_child_messages')),
            ],
            options={
                'ordering': ['-sent_at', '-id'],
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
    ]
