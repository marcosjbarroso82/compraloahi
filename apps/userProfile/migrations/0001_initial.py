# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('number', models.BigIntegerField()),
                ('type', models.CharField(max_length=200, choices=[('TEL', 'Telefono'), ('CEL', 'Celular'), ('FAX', 'Fax')])),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('slug', models.SlugField(auto_created=True)),
                ('logo', models.ImageField(upload_to='logo', blank=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('slogan', models.TextField()),
                ('style', django_pgjson.fields.JsonField(default={'background_color': '#f9f9f9', 'column': 4, 'font_color': '#00000'})),
                ('status', models.IntegerField(default=0, choices=[(0, 'deactivate'), (1, 'activate')])),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('radius', models.IntegerField(default=5000)),
                ('is_address', models.BooleanField(default=False)),
                ('address', django_pgjson.fields.JsonField(default={'nro': '', 'administrative_area_level_1': '', 'address': '', 'locality': '', 'administrative_area_level_2': '', 'country': ''})),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to='profile', default='profile/default.jpg')),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('privacy_settings', django_pgjson.fields.JsonField(default={'show_address': True})),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
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
            field=models.OneToOneField(related_name='store', to='userProfile.UserProfile'),
        ),
        migrations.AddField(
            model_name='phone',
            name='userProfile',
            field=models.ForeignKey(to='userProfile.UserProfile', related_name='phones'),
        ),
    ]
