# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_auto_20150513_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('logo', models.ImageField(default='logo/default.png', upload_to='logo')),
                ('name', models.CharField(max_length=255, default='Name')),
                ('column', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('profile', models.OneToOneField(to='userProfile.UserProfile', related_name='store')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile/default.png', upload_to='profile'),
            preserve_default=True,
        ),
    ]
