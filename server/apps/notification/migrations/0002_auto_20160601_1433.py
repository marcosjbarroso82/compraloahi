# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confignotification',
            name='config',
            field=django_pgjson.fields.JsonField(default={'cal': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando tiene tiene la posibilidad de calificar a otro usuario'}, 'cmmt': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando commentan un aviso propio'}, 'fav': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando agregan un aviso propio a favoritos'}, 'msg': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando recibe un mensaje'}, 'post': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando hacen publicaciones en los grupos a los que pertenece'}, 'prox': {'alert': True, 'email': True, 'label': 'Desea recibir una notificacion cuando estas cerca de uno de tus avisos favoritos'}}),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('msg', 'Message'), ('fav', 'Favorite'), ('cmmt', 'Comment'), ('prox', 'Near Favorite'), ('cal', 'Calification'), ('membership', 'Membership'), ('post', 'GroupPost')], max_length=20),
        ),
    ]
