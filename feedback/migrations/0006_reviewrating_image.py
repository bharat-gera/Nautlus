# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_remove_reviewrating_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='image',
            field=models.ImageField(upload_to=b'review_images', null=True, verbose_name='Image', blank=True),
            preserve_default=True,
        ),
    ]
