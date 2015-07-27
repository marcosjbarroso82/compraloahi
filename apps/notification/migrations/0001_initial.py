# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('config', django_pgjson.fields.JsonField(default={'cal': {'label': 'Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario', 'email': True, 'alert': True}, 'cmmt': {'label': 'Desea recibir una notificacion cuando commentan un aviso propio', 'email': True, 'alert': True}, 'fav': {'label': 'Desea recibir una notificacion cuando agregan un aviso propio a favoritos', 'email': True, 'alert': True}, 'msg': {'label': 'Desea recibir una notificacion cuando recibe un mensaje', 'email': True, 'alert': True}, 'prox': {'label': 'Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos', 'email': True, 'alert': True}})),
                ('user', models.OneToOneField(related_name='config_notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment'), ('prox', 'Near Favorite'), ('cal', 'Calification')], max_length=20)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('extras', django_pgjson.fields.JsonField()),
                ('read', models.DateTimeField(null=True, blank=True)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
                'ordering': ['-created'],
            },
        ),
    ]
