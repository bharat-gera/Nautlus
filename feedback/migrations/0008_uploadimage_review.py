# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_remove_reviewrating_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='review',
            field=models.ForeignKey(blank=True, to='feedback.ReviewRating', null=True),
            preserve_default=True,
        ),
    ]
