# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20151105_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.CharField(default='recharge', max_length=64, verbose_name='Shop Type', choices=[(b'recharge', 'Recharge')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.FloatField(verbose_name="User's Shop"),
        ),
    ]
