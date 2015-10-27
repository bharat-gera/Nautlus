# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beenhere',
            name='place',
            field=models.ForeignKey(to='search.PlaceDetail', db_column=b'place_id'),
        ),
        migrations.AlterField(
            model_name='bookmarked',
            name='place',
            field=models.ForeignKey(to='search.PlaceDetail', db_column=b'place_id'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='place',
            field=models.ForeignKey(to='search.PlaceDetail', db_column=b'place_id'),
        ),
    ]
