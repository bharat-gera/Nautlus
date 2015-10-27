# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(max_length=10, verbose_name='Rating')),
                ('place_id', models.CharField(max_length=1024, verbose_name='Place ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Rating Location', geography=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='Comment')),
                ('tag_friend', models.CharField(max_length=1024, null=True, verbose_name='Tag Friends', blank=True)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Deleted Comment')),
                ('like_count', models.IntegerField(default=0, max_length=100, verbose_name='like count')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewLike',
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
            name='ReviewRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_detail', models.TextField(verbose_name='Review')),
                ('rating', models.DecimalField(verbose_name='Rating', max_digits=2, decimal_places=1)),
                ('with_whom', models.CharField(max_length=1024, null=True, verbose_name='With Friend', blank=True)),
                ('tag_friend', models.CharField(max_length=1024, null=True, verbose_name='Tag Friends', blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(help_text=b'Format:Point(lat lng)', srid=4326, verbose_name='Review Location', geography=True)),
                ('is_verified', models.BooleanField(default=False, verbose_name='Review Verified')),
                ('is_credited', models.BooleanField(default=False, verbose_name='Credit on reviews')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Deleted Review')),
                ('comment_count', models.IntegerField(default=0, max_length=100, verbose_name='comment count')),
                ('like_count', models.IntegerField(default=0, max_length=100, verbose_name='like count')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(to='search.PlaceDetail', db_column=b'place_id')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedback',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reviewlike',
            name='review',
            field=models.ForeignKey(related_name=b'like_review', to='feedback.ReviewRating'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reviewcomment',
            name='review',
            field=models.ForeignKey(related_name=b'comment', to='feedback.ReviewRating'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(related_name=b'like_comment', to='feedback.ReviewComment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentlike',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
