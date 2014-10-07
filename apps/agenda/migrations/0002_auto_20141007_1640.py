# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='friday',
            field=models.OneToOneField(related_name='friday', null=True, to='agenda.Day'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='monday',
            field=models.OneToOneField(related_name='monday', null=True, to='agenda.Day'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='saturday',
            field=models.OneToOneField(related_name='saturday', null=True, to='agenda.Day'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='sunday',
            field=models.OneToOneField(related_name='sunday', null=True, to='agenda.Day'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='thursday',
            field=models.OneToOneField(related_name='thursday', null=True, to='agenda.Day'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='tuesday',
            field=models.OneToOneField(related_name='tuesday', null=True, to='agenda.Day'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='wednesday',
            field=models.OneToOneField(related_name='wednesday', null=True, to='agenda.Day'),
        ),
    ]
