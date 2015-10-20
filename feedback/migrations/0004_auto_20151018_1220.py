# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20151018_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name='Review Location', geography=True),
        ),
    ]
