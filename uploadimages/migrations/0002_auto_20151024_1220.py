# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadimages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='place',
            field=models.ForeignKey(related_name=b'place_image', db_column=b'place_id', to='search.PlaceDetail'),
        ),
    ]
