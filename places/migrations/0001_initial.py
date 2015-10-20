# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beenhere',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_id', models.CharField(max_length=128, verbose_name='Been Here')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bookmarked',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_id', models.CharField(max_length=128, verbose_name='Place ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_id', models.CharField(max_length=128, verbose_name='Been Here')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
            bases=(models.Model,),
        ),
    ]
