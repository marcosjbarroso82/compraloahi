# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment'), ('prox', 'Near Favorite')], max_length=20)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('extras', models.TextField()),
                ('read', models.DateTimeField(blank=True, null=True)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ad',
                'ordering': ['-created'],
                'verbose_name_plural': 'Ads',
            },
            bases=(models.Model,),
        ),
    ]
