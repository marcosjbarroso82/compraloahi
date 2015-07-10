# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('number', models.BigIntegerField()),
                ('type', models.CharField(choices=[('TEL', 'Telefono'), ('CEL', 'Celular'), ('FAX', 'Fax')], max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('logo', models.ImageField(blank=True, upload_to='logo')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('slogan', models.TextField()),
                ('style', django_pgjson.fields.JsonField(default={'column': 4, 'background_color': '#f9f9f9', 'font_color': '#00000'})),
                ('status', models.IntegerField(choices=[(0, 'deactivate'), (1, 'activate')], default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(default='profile/default.jpg', upload_to='profile')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userlocation',
            name='userProfile',
            field=models.ForeignKey(to='userProfile.UserProfile', related_name='locations'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='profile',
            field=models.OneToOneField(to='userProfile.UserProfile', related_name='store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phone',
            name='userProfile',
            field=models.ForeignKey(to='userProfile.UserProfile', related_name='phones'),
            preserve_default=True,
        ),
    ]
