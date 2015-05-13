# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0003_auto_20150511_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('rate', models.DecimalField(null=True, decimal_places=1, max_digits=6)),
                ('user', models.ForeignKey(unique=True, related_name='user_rating', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
