# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20151230_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fblogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fb_id', models.CharField(max_length=128, verbose_name='Facebook ID')),
                ('owner', models.OneToOneField(related_name='fb_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(blank=True, max_length=128, verbose_name='Password', validators=[django.core.validators.MinLengthValidator(6)]),
            preserve_default=True,
        ),
    ]
