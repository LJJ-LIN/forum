# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20180321_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]
