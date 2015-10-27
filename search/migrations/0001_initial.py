# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(unique=True, max_length=128, verbose_name='Category Name')),
                ('description', models.TextField(verbose_name='Category Desc')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Category')),
                ('image', models.ImageField(upload_to=b'categories', null=True, verbose_name='Image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceDetail',
            fields=[
                ('place_id', models.CharField(max_length=1024, unique=True, serialize=False, verbose_name='Place ID', primary_key=True)),
                ('place_name', models.CharField(max_length=128, verbose_name='Place Name', blank=True)),
                ('address', models.CharField(max_length=1024, null=True, verbose_name='Address', blank=True)),
                ('state', models.CharField(max_length=64, verbose_name='State', blank=True)),
                ('country', models.CharField(max_length=64, verbose_name='Country', blank=True)),
                ('postcode', models.CharField(max_length=30, verbose_name='Post Code', blank=True)),
                ('opening_hours', models.CharField(max_length=1024, null=True, verbose_name='Opening Hours', blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True, null=True, verbose_name='Coordinates', blank=True)),
                ('open_now', models.BooleanField(default=False, verbose_name='Open Now')),
                ('types', models.CharField(max_length=1024, null=True, verbose_name='Place Types', blank=True)),
                ('icon', models.CharField(max_length=1024, null=True, verbose_name='Place Icon', blank=True)),
                ('phone_number', models.CharField(max_length=64, null=True, verbose_name='Phone Number', blank=True)),
                ('web_link', models.CharField(max_length=1024, null=True, verbose_name='Web Link', blank=True)),
                ('place_tags', models.TextField(verbose_name='Place Tags', blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('category', models.ForeignKey(blank=True, to='search.PlaceCategory', null=True)),
            ],
            options={
                'verbose_name': 'Place Search',
                'verbose_name_plural': 'Places Search',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportError',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('error', models.TextField(verbose_name='Report Error')),
                ('address', models.BooleanField(default=False, verbose_name='Place Address')),
                ('opening_hours', models.BooleanField(default=False, verbose_name='Place Opening Hours')),
                ('phone_number', models.BooleanField(default=False, verbose_name='Place Phone Number')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('place', models.ForeignKey(related_name=b'place_ref_error', to='search.PlaceDetail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
