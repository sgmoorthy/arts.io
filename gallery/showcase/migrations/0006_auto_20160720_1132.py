# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0005_auto_20160717_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='gallery',
            name='rank',
            field=models.FloatField(default=0.0),
        ),
    ]