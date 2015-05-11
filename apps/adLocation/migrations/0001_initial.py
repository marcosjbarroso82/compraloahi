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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('administrative_area_level_1', models.CharField(blank=True, max_length=40, null=True)),
                ('administrative_area_level_2', models.CharField(blank=True, max_length=40, null=True)),
                ('locality', models.CharField(blank=True, max_length=40, null=True)),
                ('ad', models.ForeignKey(unique=True, related_name='locations', to='ad.Ad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
