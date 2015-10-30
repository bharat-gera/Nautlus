# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20151029_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followfriends',
            old_name='owner',
            new_name='follower',
        ),
    ]
