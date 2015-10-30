# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_followfriends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followfriends',
            name='following',
            field=models.ForeignKey(related_name=b'following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followfriends',
            name='owner',
            field=models.ForeignKey(related_name=b'follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
