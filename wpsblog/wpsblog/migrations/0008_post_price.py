# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0007_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.PositiveIntegerField(default=10000),
            preserve_default=False,
        ),
    ]