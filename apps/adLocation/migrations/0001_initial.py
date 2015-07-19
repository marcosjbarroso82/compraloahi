# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('country', models.CharField(null=True, max_length=40, blank=True)),
                ('administrative_area_level_1', models.CharField(null=True, max_length=40, blank=True)),
                ('administrative_area_level_2', models.CharField(null=True, max_length=40, blank=True)),
                ('locality', models.CharField(null=True, max_length=40, blank=True)),
                ('ad', models.ForeignKey(to='ad.Ad', related_name='locations')),
            ],
        ),
    ]
