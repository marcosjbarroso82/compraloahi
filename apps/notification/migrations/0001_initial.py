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
            name='ConfigNotification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('config', django_pgjson.fields.JsonField(default={'cmmt': {'alert': True, 'label': 'Desea recibir una notificacion cuando commentan un aviso propio', 'email': True}, 'cal': {'alert': True, 'label': 'Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario', 'email': True}, 'prox': {'alert': True, 'label': 'Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos', 'email': True}, 'msg': {'alert': True, 'label': 'Desea recibir una notificacion cuando recibe un mensaje', 'email': True}, 'fav': {'alert': True, 'label': 'Desea recibir una notificacion cuando agregan un aviso propio a favoritos', 'email': True}})),
                ('user', models.OneToOneField(related_name='config_notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('type', models.CharField(max_length=20, choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment'), ('prox', 'Near Favorite'), ('cal', 'Calification')])),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('extras', django_pgjson.fields.JsonField()),
                ('read', models.DateTimeField(null=True, blank=True)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Notifications',
                'verbose_name': 'Notification',
                'ordering': ['-created'],
            },
        ),
    ]
