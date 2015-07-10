# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallRating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('rate', models.DecimalField(max_digits=6, decimal_places=1, null=True)),
                ('user', models.ForeignKey(related_name='user_rating', unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('transaction_id', models.PositiveIntegerField()),
                ('state', models.IntegerField(default=0, choices=[(0, 'Pendiente'), (1, 'Aceptado'), (2, 'Anulado')])),
                ('rate', models.PositiveIntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Medium'), (4, 'Good'), (5, 'Very Good')], null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('voted', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_voted')),
                ('voter', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_voter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
