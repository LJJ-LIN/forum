# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-23 13:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400, verbose_name='内容')),
                ('link', models.CharField(max_length=400, verbose_name='链接')),
                ('status', models.IntegerField(choices=[(0, '未读'), (1, '已读')], default=0, verbose_name='状态')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
    ]
