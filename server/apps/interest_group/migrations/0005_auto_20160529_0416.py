# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 04:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interest_group', '0004_auto_20160526_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('role', models.IntegerField(choices=[(0, 'admin'), (1, 'member')], default=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='interest_group.InterestGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='MemberShipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('hash_validation', models.TextField(unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Pedido'), (1, 'Preaprobado'), (2, 'Aceptado'), (3, 'Rechazado'), (4, 'Expirado')], default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_requests', to='interest_group.InterestGroup')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='suscription',
            name='group',
        ),
        migrations.RemoveField(
            model_name='suscription',
            name='user',
        ),
        migrations.DeleteModel(
            name='Suscription',
        ),
    ]
