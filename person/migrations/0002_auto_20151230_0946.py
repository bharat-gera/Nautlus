# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='image',
            field=models.ImageField(default=b'person/profile-image/default.jpg', null=True, upload_to=person.models.profile_image_path, blank=True),
            preserve_default=True,
        ),
    ]
