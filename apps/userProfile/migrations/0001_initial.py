# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('number', models.IntegerField()),
                ('type', models.CharField(max_length=200, choices=[('TEL', 'Telefono'), ('CEL', 'Celular'), ('FAX', 'Fax')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('logo', models.ImageField(default='logo/default.png', upload_to='logo')),
                ('name', models.CharField(max_length=255, default='Name')),
                ('slogan', models.TextField()),
                ('style', django_pgjson.fields.JsonField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('radius', models.IntegerField(default=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(default='profile/default.png', upload_to='profile')),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userlocation',
            name='userProfile',
            field=models.ForeignKey(related_name='locations', to='userProfile.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='profile',
            field=models.OneToOneField(related_name='store', to='userProfile.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phone',
            name='userProfile',
            field=models.ForeignKey(related_name='phones', to='userProfile.UserProfile'),
            preserve_default=True,
        ),
    ]
