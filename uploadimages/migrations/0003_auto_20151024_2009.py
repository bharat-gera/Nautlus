# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uploadimages', '0002_auto_20151024_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Review Location', geography=True),
        ),
    ]
