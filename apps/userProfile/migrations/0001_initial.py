# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.BigIntegerField()),
                ('type', models.CharField(choices=[('TEL', 'Telefono'), ('CEL', 'Celular'), ('FAX', 'Fax')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('logo', models.ImageField(upload_to='logo', blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, populate_from='name', editable=False)),
                ('slogan', models.TextField()),
                ('style', django_pgjson.fields.JsonField(default={'font_color': '#00000', 'background_color': '#f9f9f9', 'column': 4})),
                ('status', models.IntegerField(default=0, choices=[(0, 'deactivate'), (1, 'activate')])),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('radius', models.IntegerField(default=5000)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='profile', default='profile/default.jpg')),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
        ),
        migrations.AddField(
            model_name='userlocation',
            name='userProfile',
            field=models.ForeignKey(to='userProfile.UserProfile', related_name='locations'),
        ),
        migrations.AddField(
            model_name='store',
            name='profile',
            field=models.OneToOneField(to='userProfile.UserProfile', related_name='store'),
        ),
        migrations.AddField(
            model_name='phone',
            name='userProfile',
            field=models.ForeignKey(to='userProfile.UserProfile', related_name='phones'),
        ),
    ]
