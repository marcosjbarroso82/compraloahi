# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('config', django_pgjson.fields.JsonField(default={'msg': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando recibe un mensaje'}, 'cmmt': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando commentan un aviso propio'}, 'fav': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando agregan un aviso propio a favoritos'}, 'prox': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos'}, 'cal': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario'}})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='config_notifications')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment'), ('prox', 'Near Favorite'), ('cal', 'Calification')], max_length=20)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('extras', models.TextField()),
                ('read', models.DateTimeField(blank=True, null=True)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ads',
                'verbose_name': 'Ad',
                'ordering': ['-created'],
            },
        ),
    ]
