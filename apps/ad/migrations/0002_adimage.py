# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('ad_id', models.ForeignKey(related_name='images', to='ad.Ad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
