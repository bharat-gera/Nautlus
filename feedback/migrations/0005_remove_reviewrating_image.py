# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20151018_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='image',
        ),
    ]
