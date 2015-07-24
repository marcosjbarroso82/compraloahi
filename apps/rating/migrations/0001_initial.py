# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallRating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('rate', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('user', models.ForeignKey(unique=True, related_name='user_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('transaction_id', models.PositiveIntegerField()),
                ('state', models.IntegerField(default=0, choices=[(0, 'Pendiente'), (1, 'Aceptado'), (2, 'Anulado')])),
                ('rate', models.PositiveIntegerField(null=True, choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Medium'), (4, 'Good'), (5, 'Very Good')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('voted', models.ForeignKey(related_name='user_voted', to=settings.AUTH_USER_MODEL)),
                ('voter', models.ForeignKey(related_name='user_voter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
