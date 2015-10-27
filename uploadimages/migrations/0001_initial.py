# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0001_initial'),
        ('feedback', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='Comment')),
                ('tag_friend', models.CharField(max_length=1024, null=True, verbose_name='Tag Friends', blank=True)),
                ('like_count', models.IntegerField(default=0, max_length=100, verbose_name='like count')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Deleted Comment')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'ImageComment',
                'verbose_name_plural': 'ImageComments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageCommentLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('image_comment', models.ForeignKey(related_name=b'like_image_comment', to='uploadimages.ImageComment')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'upload_images', null=True, verbose_name='Image')),
                ('google_images', models.TextField(null=True, verbose_name='Google Images')),
                ('review_images', models.ImageField(upload_to=b'upload_images', null=True, verbose_name='Review Image')),
                ('tag_friend', models.CharField(max_length=1024, null=True, verbose_name='Tag Friends', blank=True)),
                ('special_feature', models.TextField(max_length=1024, null=True, verbose_name='Special Feature', blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name='Review Location', geography=True)),
                ('is_verified', models.BooleanField(default=False, verbose_name='Upload Image Verified')),
                ('is_credited', models.BooleanField(default=False, verbose_name='Credit on Uploaded Image')),
                ('comment_count', models.IntegerField(default=0, max_length=100, verbose_name='comment count')),
                ('like_count', models.IntegerField(default=0, max_length=100, verbose_name='like count')),
                ('with_whom', models.CharField(max_length=1024, null=True, verbose_name='With Friend', blank=True)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Deleted Image')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('place', models.ForeignKey(to='search.PlaceDetail', db_column=b'place_id')),
                ('review', models.ForeignKey(to='feedback.ReviewRating', null=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'UploadImage',
                'verbose_name_plural': 'UploadImages',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagelike',
            name='upload_image',
            field=models.ForeignKey(related_name=b'like_image', to='uploadimages.UploadImage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagecomment',
            name='upload_image',
            field=models.ForeignKey(related_name=b'image_comment', to='uploadimages.UploadImage'),
            preserve_default=True,
        ),
    ]
