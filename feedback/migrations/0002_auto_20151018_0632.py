# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='google_images',
            field=models.TextField(null=True, verbose_name='Google Images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to=b'upload_images', null=True, verbose_name='Image'),
        ),
    ]
