# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160216_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='News',
            new_name='news_detail',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='Source',
            new_name='source',
        ),
    ]