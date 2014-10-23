# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('userProfile', models.ForeignKey(related_name='locations', unique=True, to='userProfile.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
