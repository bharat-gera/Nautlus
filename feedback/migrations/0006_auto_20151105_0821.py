# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20151104_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
