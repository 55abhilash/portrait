# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 14:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0011_auto_20170407_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='taskname',
            field=models.CharField(default='tmp', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='status_last_update',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 22, 14, 17, 36, 184954)),
        ),
    ]