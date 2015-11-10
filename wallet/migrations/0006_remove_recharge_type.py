# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_recharge_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recharge',
            name='type',
        ),
    ]
