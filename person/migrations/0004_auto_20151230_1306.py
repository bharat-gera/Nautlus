# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20151230_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fblogin',
            name='fb_id',
        ),
        migrations.AddField(
            model_name='fblogin',
            name='un_id',
            field=models.CharField(default=1, max_length=128, verbose_name='User ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fblogin',
            name='owner',
            field=models.OneToOneField(related_name='auth_login', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
