# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'Pendiente'), (1, 'Anulado'), (2, 'Aceptado')], default=0)),
                ('rate', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ad', models.ForeignKey(to='ad.Ad')),
                ('voted', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='calification_customer')),
                ('voter', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='calification_advertiserr')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
