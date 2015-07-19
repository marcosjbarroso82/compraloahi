# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('rate', models.DecimalField(max_digits=6, null=True, decimal_places=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True, related_name='user_rating')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('transaction_id', models.PositiveIntegerField()),
                ('state', models.IntegerField(default=0, choices=[(0, 'Pendiente'), (1, 'Aceptado'), (2, 'Anulado')])),
                ('rate', models.PositiveIntegerField(null=True, choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Medium'), (4, 'Good'), (5, 'Very Good')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('voted', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_voted')),
                ('voter', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_voter')),
            ],
        ),
    ]
