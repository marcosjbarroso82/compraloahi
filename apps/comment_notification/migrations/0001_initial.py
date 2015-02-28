# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0007_auto_20150225_2018'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_comments_xtd', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('type', models.TextField(max_length=20)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ad', models.ForeignKey(to='ad.Ad')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('xtd_comment', models.ForeignKey(blank=True, null=True, to='django_comments_xtd.XtdComment', related_name='xtd_comment_notifications')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
