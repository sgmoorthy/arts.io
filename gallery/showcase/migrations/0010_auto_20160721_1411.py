# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0009_auto_20160720_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpiece',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='artpiece',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]
