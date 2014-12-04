# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0004_remove_ad_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='categorytaggeditem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='categorytaggeditem',
            name='tag',
        ),
        migrations.DeleteModel(
            name='CategoryTag',
        ),
        migrations.DeleteModel(
            name='CategoryTaggedItem',
        ),
        migrations.AddField(
            model_name='ad',
            name='categories',
            field=models.ManyToManyField(to='ad.Category'),
            preserve_default=True,
        ),
    ]
