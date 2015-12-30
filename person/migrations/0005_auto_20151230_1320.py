# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20151230_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Googlelogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('un_id', models.CharField(max_length=128, verbose_name='User ID')),
                ('owner', models.OneToOneField(related_name='auth_login_google', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='fblogin',
            name='owner',
            field=models.OneToOneField(related_name='auth_login_fb', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
