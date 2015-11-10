# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(default=datetime.date(2015, 11, 5), verbose_name='Date Added', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='last_modified',
            field=models.DateTimeField(default=datetime.date(2015, 11, 5), verbose_name='Last Modified', auto_now=True),
            preserve_default=False,
        ),
    ]
