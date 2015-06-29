# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30, verbose_name='subject')),
                ('body', models.TextField(blank=True, verbose_name='body')),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='sent at')),
                ('read_at', models.DateTimeField(blank=True, verbose_name='read at', null=True)),
                ('replied_at', models.DateTimeField(blank=True, verbose_name='replied at', null=True)),
                ('sender_archived', models.BooleanField(default=False, verbose_name='archived by sender')),
                ('recipient_archived', models.BooleanField(default=False, verbose_name='archived by recipient')),
                ('sender_deleted_at', models.DateTimeField(blank=True, verbose_name='deleted by sender at', null=True)),
                ('recipient_deleted_at', models.DateTimeField(blank=True, verbose_name='deleted by recipient at', null=True)),
                ('moderation_status', models.CharField(max_length=1, default='p', verbose_name='status', choices=[('p', 'Pending'), ('a', 'Accepted'), ('r', 'Rejected')])),
                ('moderation_date', models.DateTimeField(blank=True, verbose_name='moderated at', null=True)),
                ('moderation_reason', models.CharField(max_length=120, blank=True, verbose_name='rejection reason')),
                ('parent', models.ForeignKey(verbose_name='parent message', null=True, to='msg.Msg', related_name='msg_next_messages', blank=True)),
                ('recipient', models.ForeignKey(verbose_name='recipient', null=True, to=settings.AUTH_USER_MODEL, related_name='msg_received_messages', blank=True)),
                ('sender', models.ForeignKey(verbose_name='sender', null=True, to=settings.AUTH_USER_MODEL, related_name='msg_sent_messages', blank=True)),
                ('thread', models.ForeignKey(verbose_name='root message', null=True, to='msg.Msg', related_name='msg_child_messages', blank=True)),
            ],
            options={
                'ordering': ['-sent_at', '-id'],
                'verbose_name_plural': 'messages',
                'verbose_name': 'message',
            },
            bases=(models.Model,),
        ),
    ]
