# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-07 06:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0010_auto_20170331_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='status_last_update',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 7, 6, 15, 27, 914601)),
        ),
    ]
