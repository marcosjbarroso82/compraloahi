# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('rate', models.DecimalField(null=True, decimal_places=1, max_digits=6)),
                ('user', models.ForeignKey(related_name='user_rating', unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
