# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-21 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20180311_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='status',
            field=models.IntegerField(choices=[(0, '正常'), (-1, '删除')], verbose_name='状态'),
        ),
    ]
