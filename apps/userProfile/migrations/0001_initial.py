# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('TEL', 'Telefono'), ('CEL', 'Celular'), ('FAX', 'Fax')], max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(default='profile/images.jpg', upload_to='profile')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
            model_name='phone',
            name='userProfile',
            field=models.ForeignKey(related_name='phones', to='userProfile.UserProfile'),
            preserve_default=True,
        ),
    ]