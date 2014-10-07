# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('time_begin', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='agenda',
            name='friday',
            field=models.OneToOneField(related_name='friday', to='agenda.Day'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='monday',
            field=models.OneToOneField(related_name='monday', to='agenda.Day'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='saturday',
            field=models.OneToOneField(related_name='saturday', to='agenda.Day'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='sunday',
            field=models.OneToOneField(related_name='sunday', to='agenda.Day'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='thursday',
            field=models.OneToOneField(related_name='thursday', to='agenda.Day'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='tuesday',
            field=models.OneToOneField(related_name='tuesday', to='agenda.Day'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='wednesday',
            field=models.OneToOneField(related_name='wednesday', to='agenda.Day'),
            preserve_default=True,
        ),
    ]
