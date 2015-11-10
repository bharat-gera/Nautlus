# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20151105_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='is_recharged',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
