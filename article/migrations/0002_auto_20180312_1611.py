# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-12 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ariticle',
            new_name='Article',
        ),
    ]
