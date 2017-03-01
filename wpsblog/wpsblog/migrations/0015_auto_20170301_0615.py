# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0014_remove_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='original_file',
            field=models.FileField(default=1, upload_to='uploads/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default=1273489071293804, max_length=120),
            preserve_default=False,
        ),
    ]
