# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('target_object_id', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('target_content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='favorites')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'favorites',
                'verbose_name': 'favorite',
                'ordering': ['-timestamp'],
                'get_latest_by': 'timestamp',
            },
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'target_content_type', 'target_object_id')]),
        ),
    ]
