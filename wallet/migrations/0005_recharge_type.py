# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_recharge_is_recharged'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='type',
            field=models.CharField(default='recharge', max_length=64, verbose_name='Shop Type', choices=[(b'recharge', 'Recharge')]),
            preserve_default=False,
        ),
    ]
