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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('config', django_pgjson.fields.JsonField(default={'prox': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos'}, 'msg': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando recibe un mensaje'}, 'cal': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario'}, 'cmmt': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando commentan un aviso propio'}, 'fav': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando agregan un aviso propio a favoritos'}})),
                ('user', models.OneToOneField(related_name='config_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment'), ('prox', 'Near Favorite'), ('cal', 'Calification')])),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('extras', models.TextField()),
                ('read', models.DateTimeField(null=True, blank=True)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
            },
            bases=(models.Model,),
        ),
    ]
