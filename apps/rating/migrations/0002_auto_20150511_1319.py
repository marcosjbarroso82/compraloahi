# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.PositiveIntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Medium'), (4, 'Good'), (5, 'Very Good')], null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='state',
            field=models.IntegerField(choices=[(0, 'Pendiente'), (1, 'Aceptado'), (2, 'Anulado')], default=0),
            preserve_default=True,
        ),
    ]
