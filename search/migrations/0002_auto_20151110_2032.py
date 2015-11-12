# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary_name', models.CharField(unique=True, max_length=128, verbose_name='Primary Name')),
                ('description', models.TextField(verbose_name='Category Desc')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Category')),
                ('image', models.ImageField(upload_to=b'primary_categories', null=True, verbose_name='Image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='placecategory',
            name='is_paid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='placecategory',
            name='primary_category',
            field=models.ForeignKey(default=1, to='search.PrimaryCategory'),
            preserve_default=False,
        ),
    ]
