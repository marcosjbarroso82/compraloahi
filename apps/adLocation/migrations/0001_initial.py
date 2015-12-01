# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdLocation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('address', django_pgjson.fields.JsonField(default={'nro': '', 'administrative_area_level_1': '', 'address': '', 'locality': '', 'administrative_area_level_2': '', 'country': '', 'lng': '', 'lat': ''})),
                ('ad', models.ForeignKey(to='ad.Ad', related_name='locations')),
            ],
        ),
    ]
