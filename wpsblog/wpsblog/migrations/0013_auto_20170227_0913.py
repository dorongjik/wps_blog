# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0012_auto_20170227_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_being_ad',
            field=models.BooleanField(default=False),
        ),
    ]
