# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 14:33
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_group', '0008_auto_20160530_1218'),
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adimage',
            old_name='ad_id',
            new_name='ad',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='published',
        ),
        migrations.AddField(
            model_name='ad',
            name='groups',
            field=models.ManyToManyField(related_name='items', to='interest_group.InterestGroup'),
        ),
        migrations.AddField(
            model_name='category',
            name='color',
            field=colorful.fields.RGBColorField(default='#c3c3c3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='status',
            field=models.IntegerField(choices=[(0, 'Delete'), (1, 'Active'), (2, 'Inactive')], default=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
