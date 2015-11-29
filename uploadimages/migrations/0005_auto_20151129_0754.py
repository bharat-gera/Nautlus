# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadimages', '0004_auto_20151031_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to=b'upload_images', null=True, verbose_name='Image', blank=True),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='review_images',
            field=models.ImageField(upload_to=b'upload_images', null=True, verbose_name='Review Image', blank=True),
        ),
    ]
