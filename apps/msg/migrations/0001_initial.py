# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('subject', models.CharField(verbose_name='subject', max_length=30)),
                ('body', models.TextField(blank=True, verbose_name='body')),
                ('sent_at', models.DateTimeField(verbose_name='sent at', auto_now_add=True)),
                ('read_at', models.DateTimeField(null=True, blank=True, verbose_name='read at')),
                ('replied_at', models.DateTimeField(null=True, blank=True, verbose_name='replied at')),
                ('sender_archived', models.BooleanField(default=False, verbose_name='archived by sender')),
                ('recipient_archived', models.BooleanField(default=False, verbose_name='archived by recipient')),
                ('sender_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='deleted by sender at')),
                ('recipient_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='deleted by recipient at')),
                ('moderation_status', models.CharField(default='p', verbose_name='status', max_length=1, choices=[('p', 'Pending'), ('a', 'Accepted'), ('r', 'Rejected')])),
                ('moderation_date', models.DateTimeField(null=True, blank=True, verbose_name='moderated at')),
                ('moderation_reason', models.CharField(blank=True, max_length=120, verbose_name='rejection reason')),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('parent', models.ForeignKey(blank=True, related_name='msg_next_messages', null=True, verbose_name='parent message', to='msg.Msg')),
                ('recipient', models.ForeignKey(blank=True, related_name='msg_received_messages', null=True, verbose_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, related_name='msg_sent_messages', null=True, verbose_name='sender', to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(blank=True, related_name='msg_child_messages', null=True, verbose_name='root message', to='msg.Msg')),
            ],
            options={
                'verbose_name_plural': 'messages',
                'verbose_name': 'message',
                'ordering': ['-sent_at', '-id'],
            },
        ),
    ]
